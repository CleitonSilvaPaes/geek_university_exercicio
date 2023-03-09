import os

def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False

def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'

local = os.path.dirname(os.path.realpath(__file__))
nome_do_arquivo = input('Digite o nome do arquivo: ')

nome_do_arquivo = junta_nome(nome_do_arquivo, local)

if verifica_se_existe(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arq:
            print(f'Total de linhas: {len(arq.readlines())}')
    except FileNotFoundError:
        print('Digite nome do arquivo')
else:
    print('Arquivo nao existe')
