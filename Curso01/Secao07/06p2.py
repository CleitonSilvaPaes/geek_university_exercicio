from random import randrange

n = 4

matriz1 = [[randrange(100) for i in range(n)] for j in range(n)]
matriz2 = [[randrange(100) for i in range(n)] for j in range(n)]

matriz3 = []

for i in range(len(matriz1)):
    arr = []
    for j in range(len(matriz1[i])):
        if matriz1[i][j] > matriz2[i][j]:
            arr.append(matriz1[i][j])
        else:
            arr.append(matriz2[i][j])
    matriz3.append(arr)

print('3º Matriz')
for i in matriz3:
    print(i)