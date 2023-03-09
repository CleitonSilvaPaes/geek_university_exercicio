from io import StringIO
import os

def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


local = os.path.dirname(os.path.realpath(__file__))
nome_do_arquivo1 = junta_nome(input('Digite o nome do 1° arquivo: '), local)
nome_do_arquivo2 = junta_nome(input('Digite o nome do 2° arquivo: '), local)

if verifica_se_existe(nome_do_arquivo1) and verifica_se_existe(nome_do_arquivo2):
    try:
        file = StringIO('')
        with open(nome_do_arquivo1, 'r') as arq1:
            for i in arq1.readlines():
                for j in i:
                    file.write(j)
        file.write('\n')
        with open(nome_do_arquivo2, 'r') as arq2:
            for i in arq2.readlines():
                for j in i:
                    file.write(j)
        file.seek(0)
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('Digite o nome do arquivos')
else:
    print('Arquivos nao encontrado')