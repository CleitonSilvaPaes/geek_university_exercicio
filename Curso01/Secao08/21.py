def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def primos_total(*args):
    x = args[0]
    primos = []
    primos.append(1)
    for i in range(x+1):
        count = 0
        for j in range(1, x+1):
            if i%j == 0:
                count += 1
        if count == 2:
            primos.append(i)
    return primos
    

numero = input('Digite um numero: ')
numero = isint(numero)
if numero:
    print(f'Todos os primos: ', *primos_total(*numero))
else:
    print('Digite numero valido')