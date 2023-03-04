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
    num = 1
    for i in range(n, 1, -1):
        num *= i
    return num


def fatorial_quadruplo(n):
    return (fatorial(2*n)) / (fatorial(n))


num = input('Digite o numero numero: ')
num = isint(*num)
if num:
    print(fatorial_quadruplo(*num))
else:
    print('Digite um numero valido')
