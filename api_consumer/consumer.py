import os
import requests
import json
import pandas as pd
from datetime import datetime
from utils.kms_simulator import kms_simulator as kms
from utils.load_environment import load_environment
from utils.load_to_database import load_dataframe


def get_api_data(env_name: str, endpoint: str):
    print(f'Carregando o ambiente: {env_name}')
    load_environment(env_name)

    api_url = os.getenv("API_URL")
    api_key_encrypted = os.getenv("API_KEY")
    num_requests = os.getenv('NUM_REQUESTS')
    max_payload_per_request = os.getenv('MAX_PAYLOAD_PER_REQUEST')
    max_results_per_request = os.getenv('MAX_RESULTS_PER_REQUEST')

    print(f'Realizando a requisição...')
    try:
        # Descriptografa a chave
        api_key = kms.decrypt_text(api_key_encrypted)
        
        for req in range(int(num_requests)):
            # Realiza a requisição
            now = datetime.now()
            dthr_request = now.strftime("%Y-%m-%d %H:%M:%S")

            offset = 0 if req == 0 else req * max_results_per_request
            response = requests.get(f"{api_url}/{endpoint}?apiKey={api_key}&limit={max_results_per_request}&offset={offset}")
            response.raise_for_status()
            # Obtém o json sem os metadados
            dataset = (response.json()).get('data', [])

            # Calcula o tamanho do payload (em bytes) e divide por 2.500 (custo adicional de créditos, de acordo com a documentação da API: https://pro.coincap.io/api-docs)
            payload = round(len(json.dumps(dataset, separators=(',', ':')).encode("utf-8")) / 2500, 0)
            
            print(f'Validando o payload da requisição...')
            if int(payload) <= int(max_payload_per_request):

                print('Payload válido! Inserindo dados na camada raw...')
                dataframe = pd.DataFrame(dataset)
                dataframe['updated_at'] = dthr_request

                # Normalizando nome de colunas
                df_columns = ['id', 'rank', 'symbol', 'name', 'supply', 'max_supply', 'market_cap_usd', 'volume_usd_24hr', 'price_usd',
                              'change_percent_24hr', 'vwap_24hr', 'explorer', 'updated_at' ]
                dataframe.columns = df_columns
                
                # Normalizando urls:
                dataframe['explorer'] = dataframe['explorer'].apply(lambda x: x[:x.rfind('/') + 1] if isinstance(x, str) and '/' in x else None)

                load_dataframe(dataframe = dataframe, 
                               context = endpoint, 
                               env_name = env_name,
                               schema = 'coincap_api')
            
            else:
                return f'Payload acima do permitido: Payload enviado: {payload + 1}; payload permitido: {max_payload_per_request}'
        
        print('Requisição finalizada!')
    
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a API: {e}"

