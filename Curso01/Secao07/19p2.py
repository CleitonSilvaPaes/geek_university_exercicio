"""
[mat | med_p | med_t | nf]
[mat | med_p | med_t | nf]
[mat | med_p | med_t | nf]
[mat | med_p | med_t | nf]
[mat | med_p | med_t | nf]
"""
from random import random, randrange, seed

seed(1)

matriz = []
n_linhas, n_colunas = 5, 4
for i in range(n_linhas):
    arr = []
    
    mat = 0
    med_p = round(random() * 10, 2)
    med_t = round(random() * 10, 2)
    nf = (med_p + med_t)/2
    
    rodar = True
    while rodar:
        mat = randrange(100)
        if len(matriz) != 0:
            rodar = False
        else:
            count = 0
            for i in range(len(matriz)):
                if mat in matriz[i]:
                    count+=1
            if count == 0:
                rodar = False
        
    arr.extend([mat, med_p, med_t, nf])
    matriz.append(arr)

for i in matriz:
    print(f'Matricula: {i[0]}')
    print(f'Media dos provas: {i[1]}')
    print(f'Media dos trabalhos: {i[2]}')
    print(f'Nota Final: {i[3]}')
    mef = sum(i[1:])/len(i[1:])
    print(f'Media de todas as notas: {mef}')
    print()