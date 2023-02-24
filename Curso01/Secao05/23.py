ano = int(input('Digite um ano: '))

if (ano % 400 == 0 or ano % 4 == 0) and (not ano % 100 == 0):
    print(f'Ano bissexto {ano}')
else:
    print('Nao bissexto')