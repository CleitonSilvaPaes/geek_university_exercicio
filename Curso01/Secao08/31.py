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

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

def neperiano(*args):
    n = args[0]
    soma = 1
    for i in range(n, 0, -1):
        calc = 1/fatorial(i)
        soma += calc
    return soma


nums = [input('Digite um numsero inteiro N: ')]
nums = isint(*nums)
if nums and is_positivo(*nums):
    print(neperiano(*nums))
else:
    print('Invalido, digite um numsero')