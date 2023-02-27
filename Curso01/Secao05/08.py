num1 = float(input('Digite 1 numero:'))
num2 = float(input('Digite 2 numero:'))


if not((0 <= num1 <= 10) and (0 <= num2 <= 10)):
    print('Nota Invalida')
else:
    print(f'Media: {(num1+num2)/2}')