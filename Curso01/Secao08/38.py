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


def fatorial_exponencial(*args):
    n = args[0]
    return n ** ((n-1) ** (n-2))

num = input('Digite um numero: ')
num = isint(num)
if num:
    print(fatorial_exponencial(*num))
else:
    print('Digite um numero valido')