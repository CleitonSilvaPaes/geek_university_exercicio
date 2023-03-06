def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except Exception:
            valid.append(None)
    return valid if None  not in valid else []
        

def inversa_media(*args):
    inverso = args[::-1]
    media = sum(args) / len(args)
    return inverso, media


numeros = input('Digite numeros separado por espaco: ').split()
numeros = isfloat(*numeros)

if numeros:
    print('Numero digitado: ', *numeros)
    inverso, media = inversa_media(*numeros)
    print('Invero: ', *inverso)
    print(f'Media: {media}')
else:
    print('Digite valores valido')