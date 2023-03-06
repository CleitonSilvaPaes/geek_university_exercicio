def isfloat(*args):
    valid = []
    for i in args:
        try:
            num = float(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def troque(a,b):
    a,b = b,a
    return a,b

a = input('Digite o numero A: ')
b = input('Digite o numero B: ')

if isfloat(a, b):
    a, b = isfloat(a, b)
    
    print(f'Valores original A:{a}, B:{b}\n')
    a, b = troque(a, b)
    print(f'Modificado A:{a}, B:{b}')
else:
    print('Digite valores valido')