def isint(*args):
    valid = []
    for i in args:
        try:
            nums = int(i)
            valid.append(nums)
        except TypeError:
            valid.append(None)
    return valid if None not in valid else []


def is_impar(*args):
    n = args[0]
    return True if n % 2 != 0 else False


def fatorial_duplo(n):
    values = []
    for i in range(n+1):
        if i % 2 != 0:
            values.append(i)
    num = 1
    for i in values:
        num *= i
    return num


num = input('Digite o numero numero: ')
num = isint(*num)
if num and is_impar(*num):
    print(fatorial_duplo(*num))
else:
    print('Digite um numero valido')
