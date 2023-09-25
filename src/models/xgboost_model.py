#imports
# pylint: disable=E0401
import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.metrics import mean_squared_error
from src.features.build_features_xgboost\
     import generate_time , generate_dataset_train, generate_lag



# Carregando o dataset
df = pd.read_csv(r"data\interim\MiningProcess_Flotation_Plant_Database.csv")
df = df.set_index('date')

"""
Dividindo a base, de forma que tenhamos,aprox 80% para treino e 20% para teste.

Para não ocorrer overfiting entre a semana de mudança, aumentei aproximadamente 20 linhas da amostra.
"""

# Divisão para o treino 
train = df.loc[df.index < '2017-07-24 01:00:00' ]
# Divisão para o teste 
test = df.loc[df.index >= '2017-08-20 01:00:00' ]


# Realizando um tratamento na base de treino 
train = generate_dataset_train(train)
# Criando novas features no treino 
train = generate_time(train)
train = generate_lag(train)
# Criando novas features no teste
test = generate_time(test)
test = generate_lag(test)




# Definindo features que serão utilizadas no modelo e qual a target.

X_train = train.drop(["% Iron Concentrate","% Silica Concentrate"],axis=1)
y_train = train["% Silica Concentrate"]

X_test = test.drop(["% Iron Concentrate","% Silica Concentrate"],axis=1)
y_test = test["% Silica Concentrate"]


# Usando xGBoost
reg = xgb.XGBRegressor(base_score=0.5, booster='gbtree',    
                       n_estimators=1000,
                       early_stopping_rounds=50,
                       objective='reg:linear',
                       max_depth=3,
                       learning_rate=0.01)


# Treinando o modelo
reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        verbose=100)


test['% silica_prevista'] = reg.predict(X_test)

score = np.sqrt(mean_squared_error(test['% Silica Concentrate'], test['% silica_prevista']))
print(f'RMSE Score no teste: {score:0.2f}')