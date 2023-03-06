def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []


def quantos_pares(*args):
    total = 0
    pares = []
    for i in args:
        if i % 2 == 0:
            pares.append(i)
            total +=1
    return total, pares


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
    total, numeros = quantos_pares(*numeros)
    print(f'Total de pares {total}')
    print(f'Pares: ', *numeros)
else:
    print('Digite numeros valido')
