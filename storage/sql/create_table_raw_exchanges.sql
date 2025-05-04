CREATE TABLE coincap_api.raw_exchanges (
  exchange_id varchar not null,
  name varchar not null,
  rank integer,
  percent_total_volume decimal,
  volume_usd decimal,
  trading_pairs integer,
  socket varchar,
  exchange_url varchar,
  updated varchar,
  updated_at timestamp
) PARTITION BY RANGE (updated_at)