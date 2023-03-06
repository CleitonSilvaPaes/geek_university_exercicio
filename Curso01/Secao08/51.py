from random import random


def calc_diagonal_principal(*args):
    principal = []
    
    for i in range(len(args)):
        principal.append(args[i][(len(args)-1)-i])
    return sum(principal)

n_lin, n_col = 3, 3

matriz = [[round((random() * 100), 1) for i in range(n_col)] for j in range(n_lin)]

print('Matriz')
for i in matriz:
    print(i)
    
matriz = calc_diagonal_principal(*matriz)
print(f'Soma numeros principal da diagonal: {matriz}')