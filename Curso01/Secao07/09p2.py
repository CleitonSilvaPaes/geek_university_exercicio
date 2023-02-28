from random import randrange
n = 3

matriz = [[randrange(10) for i in range(n)] for j in range(n)]

for i in matriz:
    print(i)

soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i > j and j != i:
            soma += matriz[i][j]

print(f'Soma abaixo da diagonal: {soma}')