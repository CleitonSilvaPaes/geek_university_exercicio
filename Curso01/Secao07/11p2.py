from random import randrange
n = 3

matriz = [[randrange(10) for i in range(n)] for j in range(n)]

for i in matriz:
    print(i)

soma = 0

for i in range(len(matriz)):
    soma += (matriz[i][len(matriz[i])-1-i])

print(f'Soma da diagonal segundaria: {soma}')
