from random import randrange
n = 3

matriz = [[randrange(10) for i in range(n)] for j in range(n)]

for i in matriz:
    print(i)

soma = 0

for i in range(len(matriz)):
    soma += matriz[i][i]
    # for j in range(len(matriz)):
    #     if j == i:
    #         soma += matriz[i][j]

print(f'Soma da diagonal: {soma}')