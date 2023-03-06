from random import randint

def soma_linhas(linha=0, *args):
    soma = 0

    for item in args[linha]:
        soma += item
    return soma


def isint(n):
    try:
        num = int(n)
        if num > 0:
            return num
    except Exception:
        return None

n_lin, n_col = 7, 6
matriz = [[randint(0, 10) for j in range(n_col)] for i in range(n_lin)]



num = isint(input('Digite numero: '))
if num and num <= len(matriz) :
    print('Matriz')
    for i in matriz:
        print(i)

    print(f'Soma da linha:{num}, soma:{soma_linhas(num-1, *matriz)}')
else:
    print('Digite um valor valido')
