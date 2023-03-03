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
    virar = False
    count = (n//2) + 1
    for i in range(2*n-1):
        if virar == False and i != (n//2) + 1:
            for j in range(i+1):
                pilhas += pilhas.join('*')
        else:
            virar = True
            for j in range(count+1):
                pilhas += pilhas.join('*')
            count-=1
        pilhas += pilhas.join('\n')
    pilhas = (pilhas.rstrip('\n'))
    return pilhas

num = input('Digite um numero Inteiro: ')
num = isint(num)
if num:
    print(pilha(*num))
else:
    print('Digite um numero')
    