distancia = float(input('Digite a distancia: '))
litros = float(input('Digite a quantidade de litro consumido: '))

calc = distancia / litros

if calc < 7.9:
    print('Venda o Carro!')
elif calc >= 8 or calc <= 14:
    print('Economico!')
elif calc > 12:
    print('Super Economico')