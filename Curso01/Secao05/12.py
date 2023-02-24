from math import log
num1 = int(input('Digite um numero: '))

if num1 <= 0:
    print('Numero invalido')
else:
    print(f'Logaritimo do numero: {log(num1)}')