base_maior = float(input('Digite a base maior: '))
base_menor = float(input('Digite a base menor: '))
altura = float(input('Digite a altura: '))

if base_maior > 0 and base_menor > 0:
    area = ((base_maior + base_menor) * altura)/2
    print(f'Area do trapezio: {area}')
else:
    print('Bases invalida')