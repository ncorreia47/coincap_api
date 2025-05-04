CREATE TABLE coincap_api.raw_assets (
  id varchar not null,
  rank integer,
  symbol varchar not null,
  name varchar not null,
  supply decimal,
  max_supply decimal,
  market_cap_usd decimal,
  volume_usd_24hr decimal,
  price_usd decimal,
  change_percent_24hr decimal,
  vwap_24hr decimal,
  explorer varchar,
  updated_at timestamp
) PARTITION BY RANGE (updated_at)