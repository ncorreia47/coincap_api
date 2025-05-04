# Pipeline end-to-end | Coincap API (versão 3.0)
Pipeline de dados para consumo de dados de API com informações de criptomoedas.

## Características da API
- API utilizada: CoinCap API 3.0
- 2.500 créditos gratuitos por mês (na modalidade Free Tier)
- 600 requisições por minuto
- A cada 2.500 bytes é cobrado um novo crédito (payload)
- Documentação completa: https://pro.coincap.io/api-docs

# Escopo do desenvolvimento

### Consumo dos dados via API
- Definir quais dados serão utilizados
- Construir uma função para consumir os dados, modularizando o código e garantindo a segurança de credenciais e outras informações sensíveis

### Armazenamento e transformação de dados
- Utilizar a arquitetura medalhão: raw (dados brutos), bronze (dados tratados), silver (dados modelados para entidade de negócio) e gold (cubos e métricas)
- Os dados serão persistindos em um banco PostgreSQL
- O tratamento e as transformações de dados serão realizadas com o dbt-core, utilizando SQL

### Visualização dos dados
- O dashboard será desenvolvido em PowerBI
- O objetivo do dashboards será apresentar os valores comercializados das principais criptomoedas e suas variações ao longo do tempo
- Foi utilizada a Metodologia de cargas incrementais no Powerbi, pensando em um cenário real de consumo de dados, evitando custos desnecessários de processamento dos dados e reduzindo significativamente o tempo para atualização dos dashboards
- Criada documentação para orientar o usuário na utilização dos dados do dashboard

# Instalação de pacotes e softwares utilizados

- Configuração de ambiente virtual:
```bash
python -m venv nome_da_venv
```
- Ativação do ambiente virtual (Windows):
```bash
nome_da_venv/scripts/activate
```
- Com o ambiente virtual ativado, execute o arquivo requirements.txt para instalação dos pacotes utilizados no desenvolvimento dessa aplicação:
```bash
pip install -r requirements.txt
```
- Configuração do banco Postgres (latest version):
  - Realizar o download da versão no link: https://www.postgresql.org/download/
  - Realize os procedimentos solicitados no arquivo de instalação: diretório do arquivo, porta do banco entre outras informações
  - Importante lembrar das informações de usuário, senha, porta e hostname, pois serão utilizadas nas etapas seguintes do projeto
  - Caso tenha dificuldades para realizar a instalação, acesse o tutorial disponível em: https://www.youtube.com/watch?v=jIs0LEnpRJE&t=299s

# Utilização da aplicação

### Configuração de variáveis
Os arquivos de configuração precisam seguir as seguintes convenções:
- Iniciar com dev (desenvolvimento) ou prod (produção)
- Ter a extensão .env
- Exemplo: dev.env

As seguintes variáveis precisam ser criadas para o correto funcionamento da aplicação:
```bash
# Configurações da API
API_KEY= 'Chave da API' 
API_URL= 'URL da API'
NUM_REQUESTS= 'Número de requisições'
MAX_PAYLOAD_PER_REQUEST= 'Valor máximo do payload por requisição'
MAX_RESULTS_PER_REQUEST= 'Quantidade de registros por requisição'

# Configurações do PostgreSQL
POSTGRESQL_USERNAME= 'Nome do usuário do PostgreSQL'
POSTGRESQL_PASSWORD= 'Senha do usuário do PostgreSQL'
POSTGRESQL_HOSTNAME= 'Hostname'
POSTGRESQL_PORT= 'Número da porta'
POSTGRESQL_DATABASE= 'Nome do database (banco de dados)'
```

Obs.: Importante realizar a criptografia base64 para as variáveis sensíveis, como senhas, nomes de usuários, nomes de bancos de dados e chaves de API.

### Execução da aplicação
Para realizar a extração dos dados da API e persisti-los em um banco de dados (PostgreSQL), é necessário executar os seguintes comandos no ambiente virtual configurado:

```bash
python main.py
```

Com isso, os dados serão persistidos na camada raw no banco de dados PostgreSQL.


### Configuração do dbt
O dbt será utilizado para realizar todas as etapas de transformação e carregamento dos dados para as camadas superiores (bronze, silver e gold).
Para iniciar a sua utilização, precisamos executar os seguintes comandos:

- Instalar o dbt-core e um dbt adapter (de acordo com o banco de dados utilizado) caso não tenha instalado via requirements.txt
```bash
pip install dbt-core dbt-postgres
```

Com a instalação realizada, precisamos criar o nosso projeto dentro da pasta dedicada para ele (dbt) para isolá-lo da nossa aplicação da API:

- Se o caminho do seu projeto estiver em /coincap_api/api:
```bash
cd .. # para retornar ao nível anterior
mkdir dbt # para criar a pasta
cd dbt # para entrar na pasta dbt

dbt init nome_do_seu_projeto # para criar o nome do seu projeto em dbt
```

Obs.: Se você não instalar o dbt adapter (postgres, bigquery entre outros bancos que vai utilizar) o projeto será inicializado com erro.

- Com a inicialização bem sucedida, na criação do projeto será solicitado
    - a seleção do database
    - o nome do hostname
    - a porta
    - o nome do usuário
    - a senha do usuário (não vai aparecer a senha no prompt)
    - o database_name (nome do banco de dados)
    - o nome do schema

Obs.: Essas informações serão alocadas na pasta ./dbt, no arquivo profile_template.yml

- Para validar a conexão, execute o comando abaixo:
```bash
dbt debug
```