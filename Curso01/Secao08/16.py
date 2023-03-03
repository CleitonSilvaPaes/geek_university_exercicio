def verifica_maior_zero(*args):
    valid = True
    for i in args:
        if i == None:
            valid = False
        elif  i <= 0:
            valid = False
    return valid if len(args) != 0 else False

def isint(n):
    try:
        n = int(n)
        return n
    except:
        return

def desenha_linha(n):
    return '='*n

n = input('Digite um numero inteiro: ')
n = isint(n)
if verifica_maior_zero(n):
    print(desenha_linha(n))
else:
    print('Digite um numero valido')