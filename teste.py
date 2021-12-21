import pandas as pd

#Leitura do dataset em csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv", decimal='.')
print('o tamanho do dataset é:', df.shape)

df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index('datetime')
print(df.index)

print('o tamanho do dataset é:', df.size)

#estatísticas básicas
print(df.describe())

#dataframe info
print(df.info())

#tipos de dados
print(df.dtypes)

# nomes das colunas
print(df.columns)

# seleção de uma coluna
x = df['windspeed'].mean()
print('a média da coluna windspeed', x)

y = df['temp'].mean()
print('a média da coluna temp', y)

print(('o número de locações em 2011', df[df.year==0].shape ))
print(('o número de locações em 2012', df[df.year==1].shape ))

print('o número total de locações de bike em 2011', df[df.year==0].total_count.sum())
print('o número total de locações de bike em 2012', df[df.year==1].total_count.sum())

print('A estação do ano que contém a maior média de locações',df.groupby(['season']).total_count.mean())

print('A hora do dia que contém a maior média de locações',df.groupby(['hour']).total_count.mean())

print('A estação do ano que contém a maior média de locações',df.groupby(['weekday']).total_count.mean())
print('Quarta-feira:', df[df.weekday==3].groupby(['hour']).total_count.mean().sort_values(ascending=False))
print('Sábado:', df[df.weekday==6].groupby(['hour']).total_count.mean().sort_values(ascending=False))
