def isint(*args):
    args = list(*args)
    valid = []
    for i in args:
        try:
            int(i)
            valid.append(int(i))
        except:
            valid.append(False)
    return valid if False not in valid else []
    
def calc(*args):
    return sum(*args) if sum(*args) > 0 else f'Numero invalido'

num = input('Digite um numero inteiro: ')

print(calc(isint(num)))