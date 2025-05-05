from get.consumer import Consumer

endpoints = ['assets', 'exchanges'] # Lista de endpoints para consumir os dados.
env_name = 'prod' # variáveis de ambiente carregadas

try:
    if len(endpoints) > 0 and env_name.lower() in ('dev', 'prod'): # valida se foi passado algum endpoint e um ambiente válido
        
        for endpoint in endpoints:
            Consumer.get_api_data(env_name, endpoint)
    else:
        print('Parâmtros inválidos. Requisição não realizada.')

except Exception as e:
    raise f'Erro ao consumir os dados {e}'