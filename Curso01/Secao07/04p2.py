from random import randrange

matriz = [[randrange(100) for i in range(4)] for j in range(4)]

maior = 0
pos = ()

for i in matriz:
    print(i)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == 0 and j == 0:
            maior = matriz[i][j]
        elif maior < matriz[i][j]:
            maior = matriz[i][j]
            pos = (i, j)

print(f'Maior numero encontrado: {maior}')
print(f'Posicao linha: {pos[0]}, coluna: {pos[1]}')