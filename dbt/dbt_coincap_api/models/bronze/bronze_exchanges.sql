/*
Com esses parâmetros de configuração, o dbt realizará uma instrução MERGE para atualizar os dados que têm a mesma unique_key (definida nesse modelo como uma chave
composta de cripto_id, cripto_rank, last_exchange_update e updated_at).
Além disso, foi utilizada a metodologia de contracts, para validar os tipos de dados que serão persistidos e também aplicar testes unitários.

A utilização de tags nos ajuda a identificar os modelos e permite que eles sejam executados atraves das tags 
(caso seja necessário executar todos os models com uma determianda tag)
*/
{{ config(
    materialized='incremental',
    unique_key=['cripto_id', 'cripto_rank', 'last_exchange_update', 'updated_at'],
    contracts={"enforced": true},
    on_schema_change='append_new_columns',
    tags=['bronze', 'assets']
) }}

/*
CTE para normalizar colunas para a camada bronze, sem modificar a precisão dos dados oriundos da camada raw.
O processo segue uma carga incremental, com base na partição de datas (utilizando o updated_at) criado no banco postgres.
Com a partição, é possível realizar a carga incremental e também solucionar problemas de cargas retroativas, 
como por exemplo: apagar dados de uma partição e carregá-los novamente.
*/

with bronze_exchanges as (
    select
          exchange_id                                  as cripto_id
        , upper(name)                                  as cripto_name
        , rank                                         as cripto_rank
        , percent_total_volume
        , volume_usd                                   as volume_usd_value
        , trading_pairs                                as trading_pairs_quantity
        , lower(socket)                                as fg_socket
        , exchange_url                                 as url_link
        , to_timestamp(cast(updated as bigint) / 1000) as last_exchange_update    -- convertido milesegundos para timestamp
        , '{{ run_started_at }}'::timestamp            as processed_at
        , current_timestamp::timestamp                 as updated_at
    from {{ source('raw', 'raw_exchanges') }}
    -- Realiza a carga incremental com base na partição criada no Postgres
    {% if is_incremental() %}
        where updated_at > (select max(updated_at) from {{ this }})
    {% endif %}
)

select * from bronze_exchanges