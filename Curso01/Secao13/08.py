from io import StringIO
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
            novo_texto = StringIO('')
            for i in arq.readlines():
                for j in i:
                    if j.isalpha():
                        j = j.upper()
                        novo_texto.write(j)
                    else:
                        novo_texto.write(j)
        novo_texto.seek(0)
        novo_texto.close()
    except FileNotFoundError:
        print('Digite o nome do arquivo1')
else:
    print('Arquivo nao encontrado')