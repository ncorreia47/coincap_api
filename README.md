# Case Técnico | Analytics Engineer
Pipeline de dados para consumo de dados de API com informações de criptomoedas.

## Características da API
- API utilizada: CoinCap API 3.0
- 2.500 créditos gratuitos por mês (na modalidade Free Tier)
- 600 requisições por minuto
- A cada 2.500 bytes é cobrado um novo crédito (payload)
- Documentação completa: https://pro.coincap.io/api-docs

# Escopo do desenvolvimento do Case

### Consumo dos dados via API
- Definir quais dados serão utilizados
- Construir uma função para consumir os dados, modularizando o código e garantindo a segurança de credenciais e outras informações sensíveis

### Armazenamento e transformação de dados
- Utilizar a arquitetura medalhão: raw (dados brutos), bronze (dados tratados), silver (dados modelados para entidade de negócio) e gold (cubos e métricas)
- Os dados serão persistindos em um banco PostgreSQL
- O tratamento e as transformações de dados serão realizadas com o dbt-core, utilizando SQL

### Visualização dos dados
- O dashboard será desenvolvido em PowerBI
- Quais respostas vamos tentar responder?
- Metodologia utilizada no carregamento e atualização dos dados


# Instalação de Pacotes

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

# Utilização da Aplicação

### Configuração de variáveis
Os arquivos de configuração precisam seguir as seguintes convenções:
- Iniciar com dev (desenvolvimento) ou prod (produção)
- Ter a extensão .env
- Exemplo: dev.env

As seguintes variáveis precisam ser criadas para o correto funcionamento da aplicação:
```bash
# Configurações da API
API_KEY= Chave da API 
API_URL= URL da API
NUM_REQUESTS= Número de requisições
MAX_PAYLOAD_PER_REQUEST= Valor máximo do payload por requisição
MAX_RESULTS_PER_REQUEST= Quantidade de registros por requisição

# Configurações do PostgreSQL
POSTGRESQL_USERNAME= Nome do usuário do PostgreSQL
POSTGRESQL_PASSWORD= Senha do usuário do PostgreSQL
POSTGRESQL_HOSTNAME= Hostname 
POSTGRESQL_PORT= Número da porta
POSTGRESQL_DATABASE= Nome do database (banco de dados)
```

Obs.: Importante realizar a criptografia base64 para as variáveis sensíveis, como senhas, nomes de usuários, nomes de bancos de dados e chaves de API.

### Execução da aplicação
Para realizar a extração dos dados da API e persisti-los em um banco de dados (PostgreSQL), é necessário executar os seguintes comandos no ambiente virtual configurado:

```bash
python main.py
```

Com isso, os dados serão persistidos na camada raw no banco de dados PostgreSQL