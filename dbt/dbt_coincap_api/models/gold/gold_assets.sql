/*
 CTE criada para buscar o último registro atualizado do exchanges. Com base nesses registros, podemos criar uma camada analítica de último 
 registro atualizado e compará-los com uma base histórica (persistida na camada silver).
 Criadas colunas adicionais para calculos de médias de supply_value, max_supply_value, max_cap_usd_value, volume_usd_24hr_value, price_usd_value,
 change_percent_24hr e vwap_24hr_value
 */
with last_updated_assets as (
	select
		  cripto_id
		, cripto_rank
		, cripto_symbol
		, cripto_name
		, supply_value
		, max_supply_value
		, max_cap_usd_value
		, volume_usd_24hr_value
		, price_usd_value
		, change_percent_24hr
		, vwap_24hr_value
		, avg(supply_value) over(partition by cripto_id)                     as supply_value_mean
		, avg(max_supply_value) over(partition by cripto_id)                 as max_supply_value_mean
		, avg(max_cap_usd_value) over(partition by cripto_id)                as max_cap_usd_value_mean
		, avg(volume_usd_24hr_value) over(partition by cripto_id)            as volume_usd_24hr_value_mean
		, avg(price_usd_value) over(partition by cripto_id)                  as price_usd_value_mean
		, avg(change_percent_24hr) over(partition by cripto_id)              as change_percent_24hr_mean
		, avg(vwap_24hr_value) over(partition by cripto_id)                  as vwap_24hr_value_mean
		, url_link
		, processed_at
		, updated_at
		, row_number() over(partition by cripto_id order by updated_at desc) as row_id
	
	from {{ ref('silver_assets') }})

select
      cripto_id
    , cripto_rank
    , cripto_symbol
    , cripto_name
    , supply_value
    , max_supply_value
    , max_cap_usd_value
    , volume_usd_24hr_value
    , price_usd_value
    , change_percent_24hr
    , vwap_24hr_value
    , supply_value_mean
    , max_supply_value_mean
    , max_cap_usd_value_mean
    , volume_usd_24hr_value_mean
    , price_usd_value_mean
    , change_percent_24hr_mean
    , vwap_24hr_value_mean
    , url_link
    , processed_at
    , updated_at
    
from last_updated_assets
where 1=1
and row_id = 1