# Dashboard para acompanhamento das principais criptomoedas comercializadas

O dashboard foi desenvolvido com base nos indicadores disponibilizados no site oficial da API: https://coincap.io/, com o objetivo de demonstrar o comportamento das criptomoedas ao longo do tempo.

As seguintes tabelas foram utilizadas para a construção das métricas e visualizações:

- silver_exchanges
- silver_assets
- gold_exchanges
- gold_assets

O relacionamento entre essas tabelas ocorreu através da cripto_id (silver_exchanges -> gold_exchanges) e (silver_assets -> gold_assets). O objetivo desse relacionamento foi permitir a análise detalhada ao longo do tempo dos seus registros.

Os campos utilizados foram documentados dentro do Power BI. Esses campos são:

- supply_value: Refere-se ao total de unidades (tokens ou moedas) atualmente em circulação no mercado de uma criptomoeda.
- cap_usd_value: É o valor de mercado da criptomoeda em dólares americanos (USD).
- volume_usd_24hr_value: Refere-se ao volume total negociado daquela criptomoeda nas últimas 24 horas, em dólares americanos.
- vwap_24hr_value: É o preço médio ponderado pelo volume das transações das últimas 24h.
- trading_pairs_quantity: Quantidade de pares de negociação disponíveis para essa criptomoeda em exchanges.

Em relação as tabelas:

- assets: No contexto de criptomoedas, assets são os ativos digitais negociados nas exchanges.
- exchanges: As exchanges são as plataformas onde os ativos digitais são comprados, vendidos ou trocados.


### Como acessar o dashboard?

O dashboard pode ser visualizado:
- Baixando o arquivo .pbix disponível nesse diretório; ou
- Através do link: https://app.powerbi.com/view?r=eyJrIjoiZDY4ODlkNmUtMTk3NS00YTY4LThlNDktOWQ2YWQyODBkMjMzIiwidCI6ImIwZTczMzVmLWZkMWYtNDZhZC05OGM3LTU1ZTZlNGUyMjJlYSJ9