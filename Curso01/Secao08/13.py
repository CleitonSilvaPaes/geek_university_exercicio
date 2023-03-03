import os
import time

def isfloat(*args):
    valid = []
    for i in args:
        try:
            float(i)
            valid.append(float(i))
        except:
            valid.append(None)
    return valid if None not in valid else []

def is_operacao(operacao):
    valid = ['+', '-', '*', '/']
    return operacao in valid

def calc(opracao, *args):
    x, y = args
    calculo = {
        '+': x+y,
        '-': x-y,
        '*': x*y,
        '/': x/y if y > 0 else 'Imposivel divisao por zero'
    }
    return calculo[operacao]

rodar = True
while rodar:
    numeros = []
    operacao = input('''
(+) = Soma
(-) = Subtracao
(*) = Multiplicacao
(/) = Divisao 
''')
    if is_operacao(operacao):
        x = input('Digite numero 1: ')
        y = input('Digite numero 1: ')
        numeros.extend([x, y])
        numeros = isfloat(*numeros)
        if isfloat(*numeros):
            rodar = False
            print(calc(operacao, *numeros))
        else:
            os.system('cls')
            print(f'Digite numero valido')
            time.sleep(1.2)
    else:
        os.system('cls')
        print('Digite uma operacao valida')
        time.sleep(1.2)