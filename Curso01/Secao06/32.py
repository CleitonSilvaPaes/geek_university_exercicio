from random import randint

n = int(input('Digite o numero de lancamentos: '))

for i in range(n):
    d1 = randint(0, 10)
    d2 = randint(0, 10)
    
    if d1 == d2:
        print(f'Dados iguais: {d1}')

    elif d1 > d2:
        print(f'Dado 1 maior: {d1} -- Dado 2: {d2}')

    else:
        print(f'Dado 2 maior: {d2} -- Dado 1: {d1}')
