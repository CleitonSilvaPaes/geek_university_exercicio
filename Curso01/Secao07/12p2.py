from random import randrange, seed

seed(1)

n = 3

matriz = [[randrange(10) for i in range(n)] for j in range(n)]

# Transporta
matriz2 = []
for i in range(len(matriz)):
    arr = []
    for j in range(len(matriz)):
        arr.append(matriz[j][i])
    matriz2.append(arr)

for i in matriz:
    print(i)

print('Transposta')
for i in matriz2:
    print(i)
