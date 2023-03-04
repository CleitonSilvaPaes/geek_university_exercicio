def isint(*args):
    valid = []
    for i in args:
        try:
            nums = int(i)
            valid.append(nums)
        except TypeError:
            valid.append(None)
    return valid if None not in valid else []


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)


def soma_algarismo(*args):
    n = args[0]
    n = isint(*list(str(fatorial(n))))
    return sum(n)


num = input('Digite o numrto numero: ')
num = isint(*num)
if num:
    print(soma_algarismo(*num))
else:
    print('Digite um numero valido')
