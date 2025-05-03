import os
import requests
import json
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from utils.kms_simulator import kms_simulator as kms


def load_environment(env_name: str = "dev"):
    """
        Realiza o carregamento do arquivo de variáveis de ambiente de acordo com o ambiente escolhido.
        Opções disponíveis: dev e prod
    """
    base_dir = Path(__file__).resolve().parent.parent 
    env_path = base_dir / "configs" / f"{env_name.lower()}.env"
    
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        print(f"Ambiente carregado: {env_name}")
    else:
        raise FileNotFoundError(f"Arquivo {env_path} não encontrado.")

def get_api_data(endpoint: str):
    api_url = os.getenv("API_URL")
    api_key_name = os.getenv('API_KEY_NAME')
    api_key_encrypted = os.getenv("API_KEY")
    num_requests = os.getenv('NUM_REQUESTS')
    max_payload_per_request = os.getenv('MAX_PAYLOAD_PER_REQUEST')
    max_results_per_request = os.getenv('MAX_RESULTS_PER_REQUEST')

    print(f"Realizando a requisição com a api_key_name: {api_key_name}")
    
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

            if int(payload) <= int(max_payload_per_request):
                print('Inserir dados na camada raw...')
                dataframe = pd.DataFrame(dataset)
                dataframe['updated_at'] = dthr_request
                dataframe.to_csv(f'dataframe_request_{req}.csv', sep=';', index=False) 

                print(f'Dados inseridos com sucesso na camada raw.')
            
            else:
                return f'Payload acima do permitido: Payload enviado: {payload + 1}; payload permitido: {max_payload_per_request}'
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

