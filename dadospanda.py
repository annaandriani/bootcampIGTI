import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#leitura dos dados
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
print(df.head(3))

#setando o dataset
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
print(df.index)

#estatística básica de dados numéricos
print(df.describe())

#indexação por índice
#selecionando todas as linhas e colunas
#coluna 1: temperatura

print(df .iloc[:, 1])

# indexação por nome
# selecionado todas as linhas e a coluna 1

print(df.loc[:, 'temperatura'])

#ordenação por uma coluna
print(df.sort_values(by="temperatura"))

#ordenando pelo índice
print(df.sort_index(ascending=False))

#indexação booleana, seleção de exemplos acima de 25 graus

print(df[df['temperatura'] >= 25])

#indexação booleana considerando datetime, seleção de entradas até março
print(df[df.index <= '2020-03-01'])

#plot de linhas
df.plot(style='-o', figsize=(10,5), grid=True);
plt.show(),

#pie plot
df['classification'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True, figsize=(10,7));
plt.show(),
