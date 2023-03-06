from random import random


def calc_diagonal_segundaria(*args):
    segundaria = []
    
    for i in range(len(args)):
        segundaria.append(args[i][(len(args)-1)-i])
    return sum(segundaria)

n_lin, n_col = 3, 3

matriz = [[round((random() * 100), 1) for i in range(n_col)] for j in range(n_lin)]

print('Matriz')
for i in matriz:
    print(i)
    
matriz = calc_diagonal_segundaria(*matriz)
print(f'Soma numeros segundaria da diagonal: {matriz}')