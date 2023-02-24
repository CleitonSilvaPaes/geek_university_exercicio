IMPOSTO = 0.08
ENCANADOR = 30

dias = int(input('Digite os dias trabalhado: '))

calc = (ENCANADOR - (ENCANADOR * IMPOSTO)) * dias

print(f'Valor a receber: {calc}')

