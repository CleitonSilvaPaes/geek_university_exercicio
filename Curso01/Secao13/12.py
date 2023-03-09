import os


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


local = os.path.dirname(os.path.realpath(__file__))
nome = junta_nome(input('Digite o nome do 1° arquivo: '), local)

try:
    with open(nome, encoding='utf-8') as arq:
        file = arq.readlines()
        n_linha = len(file)
        n_caracter = 0
        n_palavras = 0
        for i in file:
            tmp = i.split()
            for j in range(len(i)):
                n_caracter += 1
            for j in tmp:
                n_palavras += 1
        print(n_linha, n_caracter, n_palavras)
except FileNotFoundError:
    print('Arquivo nao encontrado!')