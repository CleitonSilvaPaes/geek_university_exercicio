def isint(*args):
    valid = []
    for i in args:
        try:
            nums = int(i)
            valid.append(nums)
        except:
            valid.append(None)
    return valid if None not in valid else []


def simplifica(*args):
    n, d = args
    if d <= 0:
        return 'Nao pode ser divizivel por 0'
    maior = n if n > d else d
    for i in range(maior, 1, -1):
        if n % i == 0 and d % i == 0:
            return f'{n//i} / {d//i}'
    return 'Ja está o maximo simplificado'


nums = [input('Digite um numsero inteiro Numerador: '), input('Digite um numsero inteiro Denominador: : ')]
nums = isint(*nums)

if nums:
    print(simplifica(*nums))
else:
    print(f'Digite numeros validos')