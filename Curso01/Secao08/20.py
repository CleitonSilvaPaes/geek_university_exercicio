def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def fatorial(*args):
    n = args[0]
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

x = input('Digite um numero: ')
x = isint(x)
if x:
    print(f'fatorial {x[0]}! = {fatorial(*x)}')
else:
    print('Digite um numero')
