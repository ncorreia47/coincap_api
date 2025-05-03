from api_consumer import consumer

consumer.load_environment('prod')
print(consumer.get_api_data('assets'))