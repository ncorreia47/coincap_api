from pathlib import Path
from dotenv import load_dotenv


class LoadEnvironment:
    
    def load_environment(self, env_name: str = "dev"):
        """
            Realiza o carregamento do arquivo de variáveis de ambiente de acordo com o ambiente escolhido.
            Opções disponíveis: dev e prod
        """
        base_dir = Path(__file__).resolve().parents[2]  # volta até o root do projeto
        env_path = base_dir / "configs" / f"{env_name.lower()}.env"
        
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, encoding="utf-8")
            print(f"Ambiente carregado: {env_name}")
        else:
            raise FileNotFoundError(f"Arquivo {env_path} não encontrado.")