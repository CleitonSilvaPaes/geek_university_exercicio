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
        vogais_sub = StringIO('')
        with open(nome_do_arquivo, 'r') as arq:     
            for i in arq.readlines():
                for j in i:
                    j = j.lower()
                    if j in 'aeiou':
                        vogais_sub.write('*')
                    else:
                        vogais_sub.write(j)
        vogais_sub.seek(0)
        print(vogais_sub.read())

            
    except FileNotFoundError:
        print('Digite nome do arquivo')
else:
    print('Arquivo nao existe')