import pandas as pd


# Carregando o dataset
df = pd.read_csv("data\processed\MiningProcess_Flotation_Plant_Database.csv",decimal=",")

# Dividindo a base, dividi a base de forma que tenhamos aprox 80% para treino e 20% para teste.
# Para não ocorrer overfiting entre a semana de mudança, aumentei 20 linhas da amostra.
# Treino
train = df.loc[df.index < '2017-07-24 01:00:00' ]

# Validação 
test = df.loc[df.index >= '2017-08-20 01:00:00' ]