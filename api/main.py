from get.consumer import Consumer

endpoints = ['assets', 'exchanges'] # Lista de endpoints para consumir os dados.
env_name = 'prod' # variáveis de ambiente carregadas

for endpoint in endpoints:
    Consumer.get_api_data(env_name, endpoint)