base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))

if base == 0 or altura == 0:
    print('Dados Invalidos')
else:
    area = (base * altura)/2
    print(f'Area do triangulo: {area}')