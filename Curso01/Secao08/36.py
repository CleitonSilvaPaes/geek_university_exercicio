def isint(*args):
    valid = []
    for i in args:
        try:
            nums = int(i)
            if nums < 0:
                valid.append(None)
            else:
                valid.append(nums)
            valid.append(nums)
        except TypeError:
            valid.append(None)
    return valid if None not in valid else []

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

def super_fatorial(*args):
    n = args[0]
    sf = 1
    for i in range(n+1):
        sf *= fatorial(i)
    return sf

num = input('Digite um numero: ')
num = isint(num)
if num:
    print(super_fatorial(*num))
else:
    print('Digite um numero valido')