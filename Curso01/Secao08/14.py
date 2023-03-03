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

def calc(*args):
    km, litros = args
    if litros <= 0:
        return 'Imposivel calcular'
    calc = km/litros
    if calc <= 8:
        return 'Venda o carro'
    if calc > 8 and calc <= 12:
        return 'Economico'
    return 'Super Economico!'
    

rodar = True
while rodar:
    numeros = [input('Digite o KM: '), input('Digite o litros gasto: ')]
    numeros = isfloat(*numeros)
    if isfloat(*numeros):
            rodar = False
            print(calc(*numeros))
    else:
        os.system('cls')
        print(f'Digite numero valido')
        time.sleep(1.2)