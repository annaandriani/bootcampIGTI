import numpy as np

a = np.array([[1,2,3], [2,3,4], [3,4,5]])
print("Array criado:\n", a)
print("shape:" , a.shape)

print("Criação de uma matriz 3x2 de 0s")
print(np.zeros((3,2)))

print("Criação de uma matriz identidade 3x2 de 1:")
print(np.ones((3,2)))

print("Criação de uma matriz identidade 3x3:")
print(np.eye(3))

print("Criação de uma matriz 3x3 com números aleatórios")
print(np.random.random((3, 3)))

#criação de uma matriz bidimensional de tamanho (3,4)
A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(A)

B = A[:2, 1:3]
print(B)

# B[0,0] aponta para a mesma posição de memória de A[0,1]
print("A[0,1] antes:")
print(A[0,1])
B[0,0] = 77
print("A[0,1] depois:")
print(A[0,1])

#Criação de uma matriz bidimensional de tamanho (3,4
A = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

#Indexação do arrau A para extração de um sub-array consistindo as primerias 2 linhas de A e das colunas de índice 1 e 2,
#resultando em um novo arrau B de tamanho (2,2:

B = A[:2, 1:3].copy() #slicing com cópia do objeto

#B[0,0] agora NÃO aponta para a mesma posição de memória de A[0,1]
print("A[0,1] antes:")
print(A[0,1])

B[0,0] = 77
print("A[0,1] depois: ")
print(A[0,1])

#arrays

x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

print("Sobrecarga de operador: ")
print(x + y)
print("Função do módulo: ")
print(np.add(x,y))
print("Soma entre um array e um escalar: ")
print(x + 10)
print("Diferença por elemento")
print(x - y)
print(np.subtract(x, y))
print("Produto por elemento")
print(x * y)
print(np.multiply(x,y))


#vetores
v = np.array([5, 5])
w = np.array([2, 3])

#produto interno de vetores
print(v.dot(w))
print(np.dot(v, w))

#produto de um vetor e uma matriz
print(x.dot(v))
print(np.dot(x, v))

#produto de matrizes
print(x.dot(v))
print(np.dot(x,y))

#divisão
print(x/y)
print(np.divide(x,y))

#raiz quadrada
print(np.sqrt(x))

#exponenciação por elemento
print(x**2)

#logaritmo por element
print(np.log(x))

