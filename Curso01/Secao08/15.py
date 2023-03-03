import os
import time


def verifica_maior_zero(*args):
    valid = True
    for i in args:
        if i <= 0:
            valid = False
    return valid if len(args) != 0 else False

def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def calc(*args):
    a, b, c = args
    if a > (b+c) or b > (a+c) or c > (a+b):
        return 'Nao forma triangulo'
    if a == b == c == a:
        return 'Triangulo equilatero'
    if (a == b) or (a == c) or (b == c):
        return 'Triangulo isosceles'
    return 'Triangulo escaleno'
    

rodar = True
while rodar:
    numeros = []
    for i in range(3):
        x = input(f'Digite numero {i + 1}: ')
        numeros.append(x)
    numeros = isfloat(*numeros)
    if verifica_maior_zero(*numeros):
        rodar = False
        print(calc(*numeros))
    else:
        os.system('cls')
        print(f'Digite um numero valido')
        time.sleep(.5)