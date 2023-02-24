valor_da_hora = float(input('Digite o valor da hora: '))
horas_trabalhadas = int(input('Quantas horas trabalhadas? '))

calc = (valor_da_hora * horas_trabalhadas) + (valor_da_hora * horas_trabalhadas) * 0.1

print(f'Valor pago com 10% a mais: {calc}')