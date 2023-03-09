import os


def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


def verifica_se_tem_um_caracter(char:str):
    return True if len(char) == 1 else False


local = os.path.dirname(os.path.realpath(__file__))
nome_do_arquivo = input('Digite o nome do arquivo: ')
nome_do_arquivo = junta_nome(nome_do_arquivo, local)

if verifica_se_existe(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arq:
            char = input('Digite o caracter: ')
            if verifica_se_tem_um_caracter(char):
                total = sum([len([j for j in i if j.lower() in char and j != '\n' ]) for i in arq.readlines()])
                print(f'Foi encotrado o caracter: {char}, no texto: {total}')
            else:
                print('Digite somente um caracter')
            
    except FileNotFoundError:
        print('Digite nome do arquivo')
else:
    print('Arquivo nao existe')