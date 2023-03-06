from random import random

def isint(n):
    try:
        n = int(n)
        if n > 1:
            return n
    except Exception:
        return None
    
 
def calc_transposta(*args):
    matriz_t = []
    for i in range(len(args)):
        arr = []
        for j in range(len(args[i])):
            arr.append(args[j][i])
        matriz_t.append(arr)

    return matriz_t
    

tam = input('Digite um numero: ')
tam = isint(tam)
if tam:
    matriz = [[round((random() * 10), 2) for j in range(tam)] for i in range(tam)]
    
    print('Matriz Original')
    for i in matriz:
        print(i)
        
    print('Matriz transposta')
    matriz = calc_transposta(*matriz)
    for i in matriz:
        print(i)    
else:
    print('Digite um numero valido')