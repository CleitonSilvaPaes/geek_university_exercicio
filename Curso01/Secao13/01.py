import os

local = os.path.dirname(os.path.realpath(__file__))
nome_arquivo = local + '\\arq.txt'

with open(nome_arquivo, 'a') as arq:
    rodar = True
    while rodar:
        txt = input('')
        if txt != '0':
            arq.write(txt)
            arq.write('\n')
        else:
            rodar = False

with open(nome_arquivo, 'r') as arq:
    [[print(j) for j in i] for i in arq.readlines()]