from random import random

n_linhas, n_coluna = 3, 6

# Matriz original
matriz = [[round(random() * 10, 1) for i in range(n_coluna)]for j in range(n_linhas)]

# Mostrando para usuario a matriz original
for i in matriz:
    print(i)

soma_impar = 0
media = []

# Calcula a soma, media, transformar a matriz
for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
        if j % 2 == 0:
            soma_impar += matriz[i][j]
        if j % 2 != 0 and j != 5:
            media.append(matriz[i][j])
        if j == 0 or j == 1:
            soma+= matriz[i][j]
    tam = len(matriz[i])-1
    matriz[i][tam] = soma

print(f'Soma de todos os elementos impares: {soma_impar}')
print(f'Media aritmetica dos elementos 2 e 4 coluna: {sum(media)/len(media)}')
print('Matriz modificada: ')
for i in matriz:
    print(i)

