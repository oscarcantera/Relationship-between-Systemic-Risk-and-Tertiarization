# The-Relationship-between-Systemic-Risk-and-Tertiarization
This study links financial and real economies by examining the relationship between financial systemic risk and the tertiarization of the real economy. Using capital structure and financial theory, it analyzes how banking stress spreads to productive sectors and increases their financial fragility.

## Description
This study examines the relationship between systemic risk in the financial system, the tertiarization of economic activity, and the financial fragility of specific business sectors. The analysis connects two dimensions:

The financial dimension, represented by the systemic risk measure known as Marginal Expected Shortfall (MES).

The real and sectoral dimension, approximated through a tertiarization proxy based on changes in the EBITDA-to-sales margin.

Sectoral financial fragility is measured using the Altman Z-Score, which serves as the dependent variable in the final regression.

## Objetives
The main objective is to analyze whether there is a statistical relationship between:

- Banking systemic risk, measured using MES.
- The operational intensity associated with tertiarization.
- Sectoral financial fragility, measured using the Altman Z-Score.

The study does not aim to establish a definitive causal relationship, but rather to examine the statistical association between these variables in the selected sample.

## Methodology
The study uses a quantitative, non-experimental approach based on secondary financial, accounting, and sectoral data. The analysis is conducted in four stages:

- Construction of the MES variable.
- Construction of the tertiarization proxy.
- Construction of the Altman Z-Score indicator.
- Integration of the variables and estimation of the final regression model.

The three variables are initially constructed independently. They are subsequently integrated using common sector and year identifiers to create a final sector-year dataset.

## Variables
### Dependent Variable 
#### Altman Z-Score
The Altman Z-Score is used as a measure of financial fragility and corporate insolvency risk. The indicator is constructed from financial ratios related to:

- Working capital to total assets.
- Retained earnings to total assets.
- EBIT to total assets.
- Market value of equity to debt.
- Sales to total assets.

The variable is initially calculated for each firm and year, after which its values are aggregated by sectoral group.

### Variables independientes
#### Marginal Expected Shortfall (MES)
MES is used as a measure of exposure to systemic financial risk. It is calculated using the returns of financial institutions and a benchmark financial index during periods of market stress. The MES variable is subsequently aggregated at an annual frequency for inclusion in the final regression model.

#### Tertiarization
The second independent variable represents the structural transformation of the economy, specifically its tertiarization. This concept is understood as the tendency of capital to shift toward sectors that are closer to final consumption. The measure is inspired by the Hayekian triangle and Roger W. Garrison’s theory of capital.

The tertiarization variable is constructed using a proxy for firm's operational intensity: the EBITDA-to-sales margin. A lower operating margin is interpreted as a greater degree of tertiarization. The variable is calculated using the EBITDA-to-sales margin for selected groups of firms, as well as its annual variation, over the selected period.

## Econometric Model 

Altman_s,t = α + β1 Δ(EBITDA/Sales)_s,t
                  + β2 MES_t
                  + β3 [Δ(EBITDA/Sales)_s,t × MES_t]
                  + ε_s,t
                  
- Altman_s,t is the annual sectoral average of the Altman Z-Score.

- Δ(EBITDA/Sales)_s,t is the annual change in the EBITDA-to-sales margin.

- MES_t is the annual measure of systemic risk.

- The interaction term makes it possible to analyze whether the effect of tertiarization changes as financial stress increases.

- ε_s,t is the error term.

## Hyphothesis
### Hyphothesis 1
A deterioration in the operating margin is associated with greater sectoral financial fragility.
### Hyphothesis 2
Greater systemic stress is associated with greater sectoral financial fragility.
### Hyphothesis 3
The effect of tertiarization on financial fragility differs when the financial system is under greater stress.

## Sample
The sample consists of publicly listed companies, mainly from the United States, grouped into four sectoral categories:

- Retail.
- Automotive.
- Telecommunications and technology.
- Energy.

The analysis period is 1997 - 2025

The unit of observation in the final regression is the sector-year. Companies are selected based on data availability, sectoral relevance, and the existence of a sufficiently long time series.

## Sources of data
The data used come from the following sources:
- To measure the MES variable, I will use data from the Federal Reserve Bank of New York: https://www.newyorkfed.org/research/banking_research/datasets.html
- To obtain historical market prices for equity securities, I will use Yahoo Finance through the yfinance Python library.
- To obtain balance-sheet and accounting data, I will use Moody’s Orbis database.
- For macroeconomic data, I will use sources such as the Federal Reserve Economic Data (FRED) database and the Bureau of Economic Analysis (BEA) website.

The download dates and the variables extracted from each source are detailed in the variable dictionaries. 
The original data are not included, either in whole or in part, when the source’s terms of use prohibit their redistribution.

## Processed Data
The dataset used in the final estimation is located at:

'data/processed/base_regresion_final.csv'

This dataset contains, at a minimum, the following variables:

- 'altman': dependent variable.
- 'delta_ebitda_sales': proxy for tertiarization.
- 'mes': independent systemic-risk variable.
- 'sector': sectoral group.
- 'year': observation year.

The processed data are generated from the data-cleaning, transformation, and integration notebooks.

## Variable Dictionary
The variable dictionary is located at:

data/diccionario_variables.xlsx

This file documents:

- The name of each variable.
- Its economic interpretation.
- Its role in the model.
- Its original source.
- Its unit of measurement.
- The formula or transformation applied.
- The treatment of missing values.
- The treatment of outliers.

## Repository Structure
 
mi_proyecto/ 
├── README.md 
├── requirements.txt 
├── .gitignore 
│ 
├── config/ 
│   ├── path.yaml   # rutas de datos (plantilla, sin credenciales) 
│   └── secrets_example.yaml # API keys, etc. (NO commitear versiones reales) 
│ 
├── src/ 
│   ├── __init__.py 
│   ├── config.py            # lee rutas desde YAML / env vars 
│   ├── data/ 
│   │   ├── load_local.py    # upload data of external sources 
│   │   ├── clean_local.py   # clean data of external sources
│   │   └── edgar_client.py  
│   ├── features/ 
│   │   └── build_features.py 
│   └── analysis/ 
│       └── descriptive_stats.py 
│ 
├── notebooks/ 
│   ├── 01_exploracion_local.ipynb 
│   ├── 02_descarga_edgar.ipynb 
│   └── 03_fusion_local_edgar.ipynb 
│   └── 04_import_chicago_fed.ipynb 
│   └── 05_econometrics.ipynb 
|   └── 06_import_avalue
|   └── 07_MES
|   └── 08_regresion_altman
|
├── docs/ 
│   ├── data_dictionary.csv 
│   └── notas_metodologicas.md 
│ 
└── results/ 
    ├── figures/ 
    └── tables/


- `notebooks/`: análisis reproducible en Jupyter.
- `src/`: funciones y scripts de Python.
- `data/`: datos de ejemplo o instrucciones de acceso.
- `results/`: tablas y gráficos generados.
- `docs/`: memoria y presentación.

External sources

data/
├── README.md
├── raw/
│   └── .gitkeep
├── interim/
│   └── .gitkeep
└── processed/
    └── .gitkeep


## Instalation 

```bash
git clone [https://github.com/usuario/nombre-repositorio.git](https://github.com/usuario/nombre-repositorio.git)
cd nombre-repositorio
pip install -r requirements.txt
```

## Perfromance

The notebooks must be run in the following order:
1. `04_import_chicago_fed.ipynb`   
2. `05_econometrics.ipynb`
3. `06_import_avalue`
4. `07_MES`
5. `08_regresion_altman`

## Results 
The results generated by the analysis are located in:

- `results/tables/`
- `results/figures/`

## Academic document
The complete dissertation for the undergraduate thesis is located at:
- docs/memoria_tfg.pdf 

## Author

Oscar Cantera Nieto

## License
This repository is published for academic purposes.