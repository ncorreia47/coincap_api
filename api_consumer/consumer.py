import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
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

    print(f"Realizando a requisição com a api_key_name: {api_key_name}")
    
    try:
        # Descriptografa a chave
        api_key = kms.decrypt_text(api_key_encrypted)

        # Realiza a requisição
        response = requests.get(f"{api_url}/{endpoint}?apiKey={api_key}")
        response.raise_for_status()
        dataset = response.json()

        # Calcula o tamanho do payload (em bytes) e divide por 2.500 (custo adicional de créditos, de acordo com a documentação da API: https://pro.coincap.io/api-docs)
        payload = round(len(json.dumps(dataset, separators=(',', ':')).encode("utf-8")) / 2500, 0)
        return f'Quantidade de créditos cobrados: {payload + 1}' # cobrança pelo payload + requisição
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

