def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []


def media(*args):
    return sum(args) / len(args)


numeros = []
rodar = True
while rodar:
    num = input('Digite um valor: ')
    numeros.append(num)
    opcao = input('Deseja continuar S/N: ').lower()
    if opcao == 'n':
        rodar = False

numeros = isfloat(*numeros)
if numeros:
    print('Numero digitados: ', *numeros)
    print(f'Media dos numeros: {media(*numeros)}')
else:
    print('Digite numeros valido')
