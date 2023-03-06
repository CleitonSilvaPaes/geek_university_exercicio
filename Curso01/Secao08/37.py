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


def hiper_fatorial(*args):
    n = args[0]
    hf = 1
    for i in range(1, n+1):
        hf *= i**i
    return hf

num = input('Digite um numero: ')
num = isint(num)
if num:
    print(hiper_fatorial(*num))
else:
    print('Digite um numero valido')