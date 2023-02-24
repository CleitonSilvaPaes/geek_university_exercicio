num1 = float(input('Digite um numero: '))

if num1 % 3 == 0 and num1 % 5 == 0:
    print('Numero invalido digite outro')
elif num1 % 3 == 0:
    print('Numero divisivel por 3')
elif num1 % 5 == 0:
    print('Numero divisivel por 5')
else:
    print('Numero nao divisevel por 3 e 5')