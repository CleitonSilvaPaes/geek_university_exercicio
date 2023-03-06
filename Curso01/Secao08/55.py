from random import randint

def soma_diagonais(*args):
    soma = 0
    for i in range(len(args)):
        soma += args[i][i]
        soma += args[i][(len(args)-1)-i]
    return soma


tam = 3
matriz = [[randint(0, 10) for j in range(tam)] for i in range(tam)]

print('Matriz')
for i in matriz:
    print(i)

print(f'Soma das diagonais: {soma_diagonais(*matriz)}')