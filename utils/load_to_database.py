import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from utils.load_environment import load_environment
from utils.kms_simulator import kms_simulator as kms


def create_connection(env_name:str):
    """
    Cria a conexão com o banco de dados, carregando as variáveis de ambiente de acordo com o ambiente informado

    Parâmetros:
        env_name (str): nome do ambiente para carregar as variáveis.
    
    Retorno:
        connection (sqlalchemy.engine.base.Engine): conexão SQLAlchemy válida.
    """

    load_environment(env_name)
    username_encrypted = os.getenv("POSTGRESQL_USERNAME")
    password_encrypted = os.getenv("POSTGRESQL_PASSWORD")
    hostname_encrypted = os.getenv("POSTGRESQL_HOSTNAME")
    port = os.getenv("POSTGRESQL_PORT")
    database_encrypted = os.getenv("POSTGRESQL_DATABASE")

    # Descriptografa as variáveis de ambiente
    username = kms.decrypt_text(username_encrypted)
    password = kms.decrypt_text(password_encrypted)
    hostname = kms.decrypt_text(hostname_encrypted)
    database = kms.decrypt_text(database_encrypted)

    # Realiza a tentativa de criar a conexão com o banco de dados    
    try:
        connection = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}', connect_args={"sslmode": "disable"})
        return connection

    except Exception as e:
        return f'Ocorreu um erro ao criar a conexão: \n{e}'


def load_dataframe(dataframe: pd.DataFrame, context: str, env_name: str, schema: str):
    """
    Realiza a inserção dos dados na camada raw (dados brutos), sempre sobrescrevendo-os a cada
    nova inserção.

    Parâmetros:
        dataframe (pd.DataFrame): dados a serem carregados.
        context (str): nome da tabela sem o prefixo (será criado como raw_<context>).
        env_name (str): nome do ambiente para carregar as variáveis.
    """

    table_name = f'raw_{context}'
    connection = create_connection(env_name)

    try:
        dataframe.to_sql(name = table_name, 
                         con = connection,
                         schema = schema,
                         if_exists = 'append', 
                         index = False, )
        print(f'{table_name} carregada com sucesso!')

    except SQLAlchemyError as e:
        print(f"Erro ao carregar a tabela '{table_name}': {e}")