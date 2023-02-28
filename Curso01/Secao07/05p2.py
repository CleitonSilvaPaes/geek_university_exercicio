from random import randrange

n = 5

matriz = [[randrange(100) for i in range(n)] for j in range(n)]

for i in matriz:
    print(i)

pos = ()

x = int(input('Digite um valor: '))

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if x == matriz[i][j]:
            pos = (i, j)

if len(pos) == 0:
    print('Nao encontrado')
else:
    print(f'Localizado linha: {pos[0]}, coluna: {pos[1]}')