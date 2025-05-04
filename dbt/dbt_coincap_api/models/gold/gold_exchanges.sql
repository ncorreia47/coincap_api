/*
 CTE criada para buscar o último registro atualizado do exchanges. Com base nesses registros, podemos criar uma camada analítica de último 
 registro atualizado e compará-los com uma base histórica (persistida na camada silver).
 Criadas colunas adicionais para calculos de médias de percent_total_volume, volume_usd_value e trading_pairs_quantity
 */
with last_updated_exchanges as (
	select
          cripto_id
        , cripto_name
        , cripto_rank
        , percent_total_volume
        , volume_usd_value
        , trading_pairs_quantity
        , avg(percent_total_volume) over(partition by cripto_id)             as percent_total_volume_mean
        , avg(volume_usd_value) over(partition by cripto_id)                 as volume_usd_value_mean
        , avg(trading_pairs_quantity) over(partition by cripto_id)           as trading_pairs_quantity_mean
        , fg_socket
        , url_link
        , last_exchange_update
        , processed_at
        , updated_at
        , row_number() over(partition by cripto_id order by updated_at desc) as row_id

from {{ ref('silver_exchanges') }})

select
      cripto_id
    , cripto_name
    , cripto_rank
    , percent_total_volume
    , volume_usd_value
    , trading_pairs_quantity
    , percent_total_volume_mean
    , volume_usd_value_mean
    , trading_pairs_quantity_mean
    , fg_socket
    , url_link
    , last_exchange_update
    , processed_at
    , updated_at
from last_updated_exchanges
where 1=1
and row_id = 1