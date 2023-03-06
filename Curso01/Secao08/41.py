def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []


def maior(*args):
    return max(args)


numeros = []
rodar = True
while rodar:
    num = input('Digite um valor: ')
    numeros.append(num)
    opcao = input('Deseja continuar S/N: ').lower()
    if opcao == 'n':
        rodar = False

numeros = isint(*numeros)
if numeros:
    print(f'Maior numero digitado: {maior(*numeros)}')
else:
    print('Digite numeros valido')
