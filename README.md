# Projeto de Mineração de Dados em Planta de Flotação
Este é um projeto de mineração de dados que visa prever a quantidade de impureza (silica) no concentrado de minério de ferro em uma planta de flotação. A capacidade de prever a quantidade de impureza em tempo real é essencial para os engenheiros da planta, pois permite que eles tomem medidas corretivas antecipadas, o que pode melhorar a qualidade do minério e reduzir o impacto ambiental ao reduzir o desperdício de minério.

# Objetivo
O principal objetivo deste projeto é desenvolver um modelo de aprendizado de máquina capaz de prever a porcentagem de sílica no concentrado de minério de ferro com base nos dados fornecidos. Isso permitirá que a equipe de engenheiros tome ações proativas para melhorar a qualidade do minério e reduzir o desperdício.

# Conjunto de Dados

O conjunto de dados utilizado neste projeto está disponível aqui: https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process.

# Visão Geral do Conjunto de Dados
O conjunto de dados consiste em várias colunas que representam diferentes variáveis relacionadas ao processo de flotação na planta. Aqui está uma breve descrição das colunas principais:
Date: Data e hora do registro.

- % Iron Feed: Porcentagem de ferro no minério de alimentação antes do processo de flotação.

- % Silica Feed: Porcentagem de sílica no minério de alimentação antes do processo de flotação.

- Starch Flow: Fluxo de amido no processo de flotação.

- Amina Flow: Fluxo de amina no processo de flotação.

- Ore Pulp Flow: Fluxo de polpa de minério no processo de flotação.

- Ore Pulp pH: pH da polpa de minério no processo de flotação.

- Ore Pulp Density: Densidade da polpa de minério no processo de flotação.

- Flotation Column 01- 07 Air Flow: Fluxo de ar na coluna de flotação 01 - 07

- Flotation Column 01 - 07 Level: Nível na coluna de flotação 01 - 07.

- % Iron Concentrate: Porcentagem de ferro no concentrado de minério após o processo de flotação.

- % Silica Concentrate: Porcentagem de sílica no concentrado de minério após o processo de flotação.
# Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py



Agradeço a EDUARDO MAGALHÃES OLIVEIRA  envolvido na coleta e disponibilização do conjunto de dados.
