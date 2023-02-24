DESCONTO = 0.10
COMISSAO = 0.05

valor = float(input('Digite o valor da compra: '))

valor_com_desconto = valor - (valor * DESCONTO)
valor_parcelado = valor/3
comissao_desconto = valor_com_desconto * COMISSAO
comissao_parcelado = valor * COMISSAO


print(f'Valor com desconto de 10%: {valor_com_desconto}')
print(f'Valor parcelado 3x sem juros: {valor_parcelado}')
print(f'Comissao da venda a vista: {comissao_desconto}')
print(f'Comissao da venda a parcelado: {comissao_parcelado}')


