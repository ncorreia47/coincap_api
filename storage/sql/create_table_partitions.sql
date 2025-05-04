CREATE TABLE coincap_api.partition_raw_assets_202505
PARTITION OF coincap_api.raw_assets
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');


CREATE TABLE coincap_api.partition_raw_exchanges_202505
PARTITION OF coincap_api.raw_exchanges
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');