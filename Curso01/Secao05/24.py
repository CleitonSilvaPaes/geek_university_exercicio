MG = 0.07
SP = 0.12
RJ = 0.15
MS = 0.08

produto = float(input('Digite o Valor do produto: '))
estado = input('Digite o estado (MG, SP, RJ, MS): ').lower()

if estado == 'mg':
    print(f'Valor do produto {produto + (produto * MG)}')
elif estado == 'sp':
    print(f'Valor do produto {produto + (produto * SP)}')
elif estado == 'rj':
    print(f'Valor do produto {produto + (produto * RJ)}')
elif estado == 'ms':
    print(f'Valor do produto {produto + (produto * MS)}')
else:
    print('Estado Invalido')

