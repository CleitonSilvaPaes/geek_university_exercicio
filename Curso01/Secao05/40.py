valor_do_carro = float(input('Digite o valor do carro: '))

if valor_do_carro <= 12000:
    calc = valor_do_carro + (valor_do_carro * 0.05)
    print(f'Custo ao consumidor: {calc}')

elif valor_do_carro > 12000 and valor_do_carro <= 25000:
    calc = valor_do_carro + (valor_do_carro * 0.1) + (valor_do_carro * 0.15)
    print(f'Custo ao consumidor: {calc}')
else:
    calc = valor_do_carro + (valor_do_carro * 0.15) + (valor_do_carro * 0.2)
    print(f'Custo ao consumidor: {calc}')