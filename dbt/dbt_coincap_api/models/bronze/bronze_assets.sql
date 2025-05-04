/*
Com esses parâmetros de configuração, o dbt realizará uma instrução MERGE para atualizar os dados que têm a mesma unique_key (definida nesse modelo como uma chave
composta de cripto_id, cripto_rank e updated_at).
Além disso, foi utilizada a metodologia de contracts, para validar os tipos de dados que serão persistidos e também aplicar testes unitários.

A utilização de tags nos ajuda a identificar os modelos e permite que eles sejam executados atraves das tags 
(caso seja necessário executar todos os models com uma determianda tag)
*/
{{ config(
    materialized='incremental',
    unique_key=['cripto_id', 'cripto_rank', 'updated_at'],
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

with bronze_assets as (
    select
          id                                as cripto_id
        , rank                              as cripto_rank
        , symbol                            as cripto_symbol
        , upper(name)                       as cripto_name
        , supply                            as supply_value
        , max_supply                        as max_supply_value
        , market_cap_usd                    as max_cap_usd_value
        , volume_usd_24hr                   as volume_usd_24hr_value
        , price_usd                         as price_usd_value
        , change_percent_24hr
        , vwap_24hr                         as vwap_24hr_value
        , explorer                          as url_link
        , '{{ run_started_at }}'::timestamp as processed_at
        , current_timestamp::timestamp      as updated_at
    from {{ source('raw', 'raw_assets') }}
    -- Realiza a carga incremental com base na partição criada no Postgres
    {% if is_incremental() %}
        where updated_at > (select max(updated_at) from {{ this }})
    {% endif %}
)

select * from bronze_assets