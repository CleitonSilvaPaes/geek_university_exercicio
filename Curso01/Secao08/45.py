def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except Exception:
            valid.append(None)
    return valid if None  not in valid else []
        

def calc_devio_padrao(*args):
    soma = 0
    media = sum(args) / len(args)
    for i in args:
        soma += (i - media) ** 2
    if (len(args)-1) == 0:
        return('Nao a desvio!')
    return round((soma / (len(args)-1)), 2)


numeros = input('Digite numeros separado por espaco: ').split()
numeros = isfloat(*numeros)
if numeros:
    print('Numeros digitados: ', *numeros)
    print(f'Devio padrao: {calc_devio_padrao(*numeros)}')
else:
    print('Digite valores valido')