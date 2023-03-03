from math import factorial

def isint(*args):
    valid = []
    for i in args:
        try:
            nums = int(i)
            valid.append(nums)
        except:
            valid.append(None)
    return valid if None not in valid else []

def is_positivo(*args):
    valid = []
    for i in args:
        if i >= 0:
            valid.append(i)
        else:
            valid.append(None)
    return True if None not in valid else False


def termo_geral(*args):
    x, n = args
    pi = 3.141593
    x = x * (pi/180)
    if n > 6 or n < -1:
        return 'N invalido aceito de 0 a 5'
    return ((-1)**n / factorial(2*n+1)) * (x**(2*n+1))


nums = [input('Digite um numsero inteiro X: '), input('Digite um numsero inteiro N: ')]
nums = isint(*nums)
if nums and is_positivo(*nums):
    print(termo_geral(*nums))
else:
    print('Invalido, digite um numsero')