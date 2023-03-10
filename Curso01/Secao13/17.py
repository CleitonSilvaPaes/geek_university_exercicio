from io import StringIO
from random import randint
from functools import reduce
import time

def isint(*args):
    valid = []
    for i in args:
        try:
            i = int(i)
            valid.append(i)
        except BaseException:
            valid.append(None)
    return valid if None not in valid else []

            
def montar_matriz_original(*args):
    args = isint(*args)
    matriz = []
    if args and len(args) == 2:
        matriz = [[1 for i in range(args[1])] for i in range(args[0])]
        return matriz
    else:
        return matriz


def total_possiveis_anuladas(*args):
    try:
        return reduce(lambda x, y: x * y, isint(*args))
    except TypeError:
        return []


def montar_matriz_saida(matriz:list, pos:list):
    pos = [isint(*i) for i in pos]
    for i in pos:
        count = 0
        for j in range(len(pos)):
            if i == pos[j]:
                count +=1
            if count > 1:
                return []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for k in range(len(pos)):
                if pos[k] == [i, j]:
                    matriz[i][j] = 0
    return matriz

with StringIO('3 3 2\n1 0\n1 2') as arq:
    file = [i.replace('\n', '').split() for i in arq.readlines()]
    matriz = montar_matriz_original(*file[0][:2])
    anuladas = isint(file[0][2])
    if matriz and anuladas:
        total_anuladas = total_possiveis_anuladas(*file[0][:2])
        anuladas = anuladas.pop()
        pos = [file[i] for i in range(1, len(file))]
        if anuladas >=0 and anuladas <= total_anuladas and anuladas == len(pos):
            matriz = montar_matriz_saida(matriz, pos)
            if matriz:
                with StringIO('') as arq2:
                    for i in matriz:
                        for j in i:
                            arq2.write(str(j)+' ')
                        arq2.write('\n')
                    arq2.seek(0)
                    print(arq2.read())
            else:
                print('Posicoes de anuladas iguais')
        else:
            print(f'Anuladas invalido tem que maior que 0 e menor {total_anuladas}')
    else:
        print('Dados invalidos!')