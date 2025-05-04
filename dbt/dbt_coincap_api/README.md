# Transformação dos dados da arquitetura medalhão (raw, bronze, silver e gold)

Com o projeto configurado, os artefatos abaixo foram desenvolvidos para simular o comportamento de um pipeline de dados utilizando o dbt.
Os dados persistidos na camada raw (através da aplicação em Python) são transformados e tratados nos <strong style="color:#6c757d">models</strong> do dbt.

## Arquitetura do projeto

### Bronze

A camada bronze foi desenvolvida seguindo a estrutura abaixo:

```bash
models/
└── bronze/
    ├── bronze_assets.sql
    ├── bronze_exchanges.sql
    └── schema.yml

```

Onde:
- bronze_assets: representa o código sql para construir a tabela bronze_assets no banco de dados, aplicando algumas transformações simples. O objetivo aqui é normalizar a tabela e manter os dados o mais próximo da realidade da origem.

- bronze_exchanges: representa o código sql para construir a tabela bronze_exchanges no banco de dados, aplicando algumas transformações simples. O objetivo aqui é normalizar a tabela e manter os dados o mais próximo da realidade da origem.

- schema.yml: arquivo de configuração onde apontamos os sources (fontes externas do dbt) e a definição do nossos models, informando metadados (como tags, proprietário, contexto entre outros) e os tipos de dados de cada coluna, assim como seus testes (unique_key, not_null e testes customizados).


### Silver

A camada silver foi desenvolvida seguindo a estrutura abaixo:

```bash
models/
└── silver/
    ├── silver_assets.sql
    ├── silver_exchanges.sql
    └── schema.yml

```

Onde:
- silver_assets: representa o código sql para construir a tabela silver_assets no banco de dados, aplicando transformações para modelagem da tabela com base no contexto da entidade de negócio: normalização de colunas, ajustes nas precisões dos dados entre outras.

- silver_exchanges: representa o código sql para construir a tabela silver_exchanges no banco de dados, aplicando transformações para modelagem da tabela com base no contexto da entidade de negócio: normalização de colunas, ajustes nas precisões dos dados entre outras.

- schema.yml: arquivo de configuração onde definimos nossos models, informando metadados (como tags, proprietário, contexto entre outros) e os tipos de dados de cada coluna, assim como seus testes (unique_key, not_null e testes customizados).


### Gold

A camada gold foi desenvolvida seguindo a estrutura abaixo:

```bash
models/
└── gold/
    ├── gold_assets.sql
    ├── gold_exchanges.sql
    └── schema.yml

```

Onde:
- gold_assets: representa o código sql para construir a tabela gold_assets no banco de dados, aplicando agrupamentos dos dados com base na última atualização e calculando a média de valores ao longo do tempo.

- gold_exchanges: representa o código sql para construir a tabela gold_exchanges no banco de dados, aplicando agrupamentos dos dados com base na última atualização e calculando a média de valores ao longo do tempo.

- schema.yml: arquivo de configuração onde definimos nossos models, informando metadados (como tags, proprietário, contexto entre outros) e os tipos de dados de cada coluna, assim como seus testes (unique_key, not_null e testes customizados).

## Exemplos de execução
Executar models da camada bronze que tem em seu configs (parte inicial da construção de um model) ou no arquivo schema.yml a tag <strong style="color:#6c757d">bronze</strong>:

```bash
dbt run --select tag:bronze

```

Executar models explicitando o nome do arquivo:

```bash
dbt run --models silver_assets

```

Executar testes de um model explicitando o nome do arquivo:

```bash
dbt test --select bronze_exchanges

```