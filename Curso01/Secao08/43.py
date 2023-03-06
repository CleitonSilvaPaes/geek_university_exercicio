from random import randrange

def isint(*args):
    valid = []
    for i in args:
        try:
            num = int(i)
            valid.append(i)
        except Exception:
            valid.append(None)
    return valid if None not in valid else []
        

def trocar_num_aleatorio(*args):
    args = list(args)
    for i in args:
        for j in range(len(args)):
            if args.count(i) >= 2:
                rodar = True
                while rodar:
                    num = randrange(0, 100)
                    if num not in args:
                        rodar = False
                        args[j] = num
    return args
                

numeros = input('Digite numeros inteiro separado por espaco:  ').split()
numeros = isint(*numeros)
if numeros:
    print('Numeros digitados: ', *numeros)
    print('Novos numeros: ', *trocar_num_aleatorio(*numeros))
else:
    print('Digite numeros validos')