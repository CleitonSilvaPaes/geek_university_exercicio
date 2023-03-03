def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def soma_entre(*args):
    x, y = args
    if x > y:
        y,x = x, y
    return sum([i for i in range(x+1, y)])

numeros = []
for i in range(2):
    x = input(f'Digite {i+1}: ')
    numeros.append(x)

numeros = isint(*numeros)
if numeros:
    print(soma_entre(*numeros))
else:
    print('Digite numero valido')