from random import random, seed

seed(1)

n_linhas, n_colunas = 3, 3

# monta a matriz
matriz = [[round(random() * 20, 0) for i in range(n_colunas)] for j in range(n_linhas)]

# Gerar array unidimencional e soma
arr = []
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz)):
        soma += matriz[j][i]
    arr.append(soma)

# Mostrar a matriz principal
for i in matriz:
    print(*i)

# Mostra a soma
print('Soma')
print(*arr)
