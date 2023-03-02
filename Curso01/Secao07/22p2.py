import os
from random import random, seed

seed(1)

n_linhas, n_coluna = 3, 3

# Matriz original 1
matrizA = [[round(random() * 10, 0) for i in range(n_coluna)]for j in range(n_linhas)]

matrizB = [[round(random() * 10, 0) for i in range(n_coluna)]for j in range(n_linhas)]

matrizC = []
for i in range(len(matrizA)):
    arr = []
    for j in range(len(matrizA[i])):
        calc = matrizA[i][j] * matrizB[i][j]
        arr.append(calc)
    matrizC.append(arr)

for i in matrizC:
    print(i)