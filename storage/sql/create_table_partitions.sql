CREATE TABLE coincap_api.partition_raw_assets_202505
PARTITION OF coincap_api.raw_assets
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_raw_exchanges_202505
PARTITION OF coincap_api.raw_exchanges
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_bronze_assets_202505
PARTITION OF coincap_api.bronze_assets
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_bronze_exchanges_202505
PARTITION OF coincap_api.bronze_exchanges
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_silver_assets_202505
PARTITION OF coincap_api.silver_assets
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_silver_exchanges_202505
PARTITION OF coincap_api.silver_exchanges
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_gold_assets_202505
PARTITION OF coincap_api.gold_assets
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');

CREATE TABLE coincap_api.partition_gold_exchanges_202505
PARTITION OF coincap_api.gold_exchanges
FOR VALUES FROM ('2025-05-01 00:00:00') TO ('2025-05-31 23:59:59');