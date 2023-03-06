from random import randint

def isint(n):
    try:
        num = int(n)
        if num > 0:
            return num
    except Exception:
        return None
    

def multiplica_matriz(**kwargs):
    matriz_a = kwargs['matriz_a']
    matriz_b = kwargs['matriz_b']
    matriz_c = []
    for i in range(len(matriz_a)):
        arr = []
        for j in range(len(matriz_a[i])):
            num = matriz_a[i][j] * matriz_b[i][j]
            arr.append(num)
        matriz_c.append(arr)
    return matriz_c

tam = isint(input('Digite o tamanho da matriz quadrada: '))
if tam:
    matriz_a = [[randint(0, 10) for j in range(tam)] for i in range(tam)]
    matriz_b = [[randint(0, 10) for j in range(tam)] for i in range(tam)]
    
    txt = 'Matriz A | Matriz_B'
    print(txt)
    for i in range(len(matriz_a)):
        print(f'{matriz_a[i]} | {matriz_b[i]}'.center(len(txt)))
    matriz_c = multiplica_matriz(matriz_a=matriz_a, matriz_b=matriz_b)
    print('Matriz C')
    for i in matriz_c:
        print(i)
    
else:
    print('Digite um valor valido')