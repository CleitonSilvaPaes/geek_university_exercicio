num1 = float(input('Digite 1 numero:'))
num2 = float(input('Digite 2 numero:'))

if num1 < num2:
    num1, num2 = num2, num1
    print(f'Maior: {num1}')
    print(f'Menor: {num2}')
elif num1 == num2:
    print('Numeros iguais')
else:
    print(f'Maior: {num1}')
    print(f'Menor: {num2}')