import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

#o modelo matemático irá aprender,a partir dessa pequena base de dados, a inferir (generalizar)

#extração de x e y
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

x, y = df[['temperatura']].values, df[['classification']].values
print("x:\n", x)
print("y:\n", y)

#conversão de y para valores numéricos
le = LabelEncoder()
y = le.fit_transform(y.ravel())
print("y:\n", y)

# classificador
clf = LogisticRegression()
clf.fit(x, y)

# gerando 100 valores de temperatura, linearmente espaçados entre 0 e 45 predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predição desses valores
y_pred = clf.predict(x_test)

# conversão de y_pred para os valores originais
y_pred = le.inverse_transform(y_pred)

output = {'new_tem': x_test.ravel(), 'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

#estatísticas
output.info()

# distribuição do output produzido com novas temperaturas a partir de um dataset com 6 exemplos
output.boxplot(by = 'new_class', figsize=(10, 5));
plt.show()
