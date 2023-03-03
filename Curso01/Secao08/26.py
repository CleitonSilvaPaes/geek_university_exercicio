def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def is_positivo(*args):
    valid = []
    for i in args:
        if i > 0:
            valid.append(i)
        else:
            valid.append(None)
    return True if None not in valid else False

def somatorio(num):
    if num == 1:
        return num
    return num + somatorio(num-1)


num = input('Digite um numero inteiro: ')
num = isint(num)
if num and is_positivo(*num):
    print(somatorio(*num))
else:
    print('Invalido, digite um numero')