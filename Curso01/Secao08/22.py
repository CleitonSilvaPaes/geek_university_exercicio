def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(num)
        except:
            valid.append(None)
    return valid if None not in valid else []

def pilha(*args):
    n = args[0]
    pilhas = str()
    for i in range(n):
        for j in range(i+1):
            pilhas += pilhas.join('!')
        pilhas += pilhas.join('\n')
    return pilhas

num = input('Digite um numero Inteiro: ')
num = isint(num)
if num:
    print(pilha(*num))
else:
    print('Digite um numero')
    