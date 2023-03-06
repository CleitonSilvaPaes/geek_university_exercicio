from random import random


def calc_abaixo_diagonal(*args):
    abaixo = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            if i > j:
                abaixo.append(args[i][j])
    return round(sum(abaixo), 2)

n_lin, n_col = 3, 3

matriz = [[round((random() * 100), 1) for i in range(n_col)] for j in range(n_lin)]

print('Matriz')
for i in matriz:
    print(i)
    
matriz = calc_abaixo_diagonal(*matriz)
print(f'Soma numeros abaixo da diagonal: {matriz}')