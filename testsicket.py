import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression

df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

# extração de x e y
x, y = df[['temperatura']].values, df[['classification']].values
print("x:\n", x)
print("y:\n", y)

# conversão de y para valores numéricos
le = LabelEncoder()  # label enconder
y = le.fit_transform(y.ravel())
print("y:\n", y)

# classificador
clf = LogisticRegression()
clf.fit(x, y)

# gerando 100 valores de temperatura
# linearmente espaçados entre 0 e 45
# predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predição desses valores
y_pred = clf.predict(x_test)

def classify_temp():
    #classificação do imput do usuário
    ask = True

    while ask:
        temp = input("Insira um valor de temperatura: ")

        #Transforma em numpy array
        temp = np.array(float(temp)).reshape(-1,1)

        #Realiza classificação
        class_temp = clf.predict(temp)

        #transformação inversa para voltar a string original
        class_temp = le.inverse_transform(class_temp)

        #classificação
        print(f"A classificação da temperatura é: {temp.ravel()[0]} é", class_temp[0])

        ask = input("a nova classificação é (y/n)") == "y"

classify_temp()
