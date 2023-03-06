from random import randint

def soma_colunas(col=0, *args):
    soma = 0

    for i in range(len(args)):
        soma += args[i][col]
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

print('Matriz')
for i in matriz:
    print(i)


num = isint(input('Digite numero da coluna: '))
if num and num <= len(matriz[0]) :
    

    print(f'Soma da coluna:{num}, soma:{soma_colunas(num-1, *matriz)}')
else:
    print('Digite um valor valido')
