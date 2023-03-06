from random import randint


def isint(n):
    try:
        n = int(n)
        if n > 1:
            return n
    except Exception:
        return None
    

def soma_elementos(*args):
    soma = 0
    for linha in args:
        for item in linha:
            soma += item
    return soma


tam = 4

matriz = [[randint(0, 100) for j in range(tam)] for i in range(tam)]
print('Matriz')
for i in matriz:
    print(i)

print(f'Soma de todos os elementos: {soma_elementos(*matriz)}')