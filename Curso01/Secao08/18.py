def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def expo(*args):
    x, y = args
    return x ** y

numeros = []
for i in range(2):
    x = input(f'Digite {i+1}: ')
    numeros.append(x)

numeros = isfloat(*numeros)
if numeros:
    print(expo(*numeros))
else:
    print('Digite numero valido')