from random import random


def maior_dez(*args):
    maiores = []
    for linha in args:
        for item in linha:
            if item > 10:
                maiores.append(item)
    return maiores

n_lin, n_col = 4, 4

matriz = [[round((random() * 100), 1) for i in range(n_col)] for j in range(n_lin)]

print('Matriz')
for i in matriz:
    print(i)
    
matriz = maior_dez(*matriz)
print('Numeros maiores que 10: ', *matriz)