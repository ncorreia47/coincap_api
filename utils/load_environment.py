from pathlib import Path
from dotenv import load_dotenv


def load_environment(env_name: str = "dev"):
    """
        Realiza o carregamento do arquivo de variáveis de ambiente de acordo com o ambiente escolhido.
        Opções disponíveis: dev e prod
    """
    base_dir = Path(__file__).resolve().parent.parent 
    env_path = base_dir / "configs" / f"{env_name.lower()}.env"
    
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, encoding="utf-8")
        print(f"Ambiente carregado: {env_name}")
    else:
        raise FileNotFoundError(f"Arquivo {env_path} não encontrado.")