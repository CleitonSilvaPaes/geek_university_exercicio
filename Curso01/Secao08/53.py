from random import randint


def isint(n):
    try:
        n = int(n)
        if n > 1:
            return n
    except Exception:
        return None
    
 
def calc_identidade(*args):
    count = 0
    for i in range(len(args)):
        if args[i][i] == 1:
            count += 1     
    return 'Identidade' if count == len(args) else 'Nao Identidade'
    

tam = input('Digite um numero: ')
tam = isint(tam)
if tam:
    matriz = [[(randint(0, 1)) for j in range(tam)] for i in range(tam)]
    for i in matriz:
        print(i)
    print(f'Matriz: {calc_identidade(*matriz)}')
else:
    print('Digite um numero valido')