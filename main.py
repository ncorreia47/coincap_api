from api_consumer import consumer

# Consumo de dados de assets
consumer.get_api_data('prod', 'assets')

# Consumo de dados de exchanges
consumer.get_api_data('prod', 'exchanges')