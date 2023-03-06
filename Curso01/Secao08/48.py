from random import random


def calc_acima_diagonal(*args):
    acima = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            if i < j:
                acima.append(args[i][j])
    return round(sum(acima), 2)

n_lin, n_col = 3, 3

matriz = [[round((random() * 100), 1) for i in range(n_col)] for j in range(n_lin)]

print('Matriz')
for i in matriz:
    print(i)
    
matriz = calc_acima_diagonal(*matriz)
print(f'Soma numeros acima da diagonal: {matriz}')