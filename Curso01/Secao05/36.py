venda = float(input('Digite o valor da venda: '))

if venda >= 100_000.000:

    calc = 700 + (venda * 0.16)
    print(f'Comissao: {calc}')

elif venda >= 80_000.00 and venda < 100_000.000:

    calc = 650 + (venda * 0.14)
    print(f'Comissao: {calc}')

elif venda >= 60_000.00 and venda < 80_000.000:

    calc = 600 + (venda * 0.14)
    print(f'Comissao: {calc}')

elif venda >= 40_000.00 and venda < 60_000.000:

    calc = 550 + (venda * 0.14)
    print(f'Comissao: {calc}')

elif venda >= 20_000.00 and venda < 40_000.000:

    calc = 500 + (venda * 0.14)
    print(f'Comissao: {calc}')

elif venda < 20_000.000:
    
    calc = 400 + (venda * 0.14)
    print(f'Comissao: {calc}')