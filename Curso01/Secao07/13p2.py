from random import randrange, seed

seed(2)

n = 4

matriz = [[randrange(1, 10) for i in range(n)] for j in range(n)]


matriz2 = []
for i in range(len(matriz)):
    arr = []
    for j in range(len(matriz)):
        if j > i and j != i:
            arr.append(0)
        else:
            arr.append(matriz[i][j])
    matriz2.append(arr)

# Original
for i in matriz:
    print(i)

# Transformada
print('Transformada')
for i in matriz2:
    print(i)
