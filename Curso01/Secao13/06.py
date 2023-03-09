import os


def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'

def isint(n):
    try:
        n = int(n)
        return n
    except:
        return 1
local = os.path.dirname(os.path.realpath(__file__))
nome_do_arquivo = input('Digite o nome do arquivo: ')
nome_do_arquivo = junta_nome(nome_do_arquivo, local)

if verifica_se_existe(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arq:
            alfabeto = {}
            for i in arq.readlines():
                for j in i:
                    j = j.lower()
                    if alfabeto.get(j) and j.isalpha():
                        alfabeto[j] += 1
                    elif j.isalpha():
                        alfabeto[j] = 1
                        
            print(dict(sorted(alfabeto.items())))
            
    except FileNotFoundError:
        print('Digite nome do arquivo')
else:
    print('Arquivo nao existe')