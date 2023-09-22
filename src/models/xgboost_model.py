#imports
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from src.features.build_features import generate_week ,\
      generate_dataset_train, generate_lag


# Carregando o dataset
df =\
pd.read_csv("data\interim\MiningProcess_Flotation_Plant_Database.csv")

""" Dividindo a base, de forma que tenhamos,
      aprox 80% para treino e 20% para teste.
 Para não ocorrer overfiting entre a semana de mudança,
    aumentei aproximadamente 20 linhas da amostra.
"""
# Divisão para o treino 
train = df.loc[df.index < '2017-07-24 01:00:00' ]

# Divisão para o teste 
test = df.loc[df.index >= '2017-08-20 01:00:00' ]

# Criando novas features no treino 
train = generate_week(train)
train = generate_lag(train)

# Criando novas features no teste
test = generate_week(test)
test = generate_lag(test)

# Realizando um tratamento na base de treino 
train = generate_dataset_train(train)



# Definindo features que serão utilizadas no modelo e qual a target.

X_train = train.drop("% Iron Concentrate","% Silica Concentrate",)
y_train = train["% Silica Concentrate"]

X_test = test.drop("% Iron Concentrate","% Silica Concentrate",)
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


# Previsões
ax = df[['consumo_mw']].plot(figsize=(15, 5))
df['consumo_previsto'].plot(ax=ax, style='.')
plt.legend(['Dados Reais', 'Previsões'])
ax.set_title('Dados reais vs Previsões')
plt.show()