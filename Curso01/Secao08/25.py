def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def serie(num):
    if num <= 0 or num == 1:
        return ((num**2)+1)/(num + 3)
    return ((num**2)+1)/(num + 3) + serie(num-1)


num = input('Digite um numero inteiro: ')
num = isint(num)
if num:
    print(serie(*num))
else:
    print('Invalido, digite um numero')