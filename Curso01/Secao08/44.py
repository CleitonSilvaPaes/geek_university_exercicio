def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except Exception:
            valid.append(None)
    return valid if None  not in valid else []
        

def pares_impares(*args):
    pares = []
    impares = []
    for i in args:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

numeros = []
for i in range(30):
    num = input(f'Digite numero {i+1}: ')
    numeros.append(num)
    
numeros = isint(*numeros)
if numeros:
    pares, impares = pares_impares(*numeros)
    print('Numeros pares: ', *pares)
    print('Numeros impares: ', *impares)
else:
    print('Digite valores validos')