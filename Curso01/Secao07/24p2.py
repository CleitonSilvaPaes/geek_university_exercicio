from random import random, seed

seed(1)

matriz_n_n = 20

matriz1 = [[round(random()*100, 0)for i in range(matriz_n_n)]for j in range(matriz_n_n)]

for i in matriz1:
    print(i)

produto = 1
maior_produto = 0
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        if j > 3 and i < 17:
            produto = matriz1[i][j] * matriz1[i+1][j-1] * matriz1[i+2][j-2] * matriz1[i+3][j-3]
            if produto > maior_produto:
                maior_produto = produto
        if j < 17:
            produto = matriz1[i][j] * matriz1[i][j+1] * matriz1[i][j+2] * matriz1[i][j+3]
            if produto > maior_produto:
                maior_produto = produto
        if j < 17 and i < 17:
            produto = matriz1[i][j]*matriz1[i+1][j+1]*matriz1[i+2][j+2]*matriz1[i+3][j+3]
print(maior_produto)