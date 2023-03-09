import os


def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


local = os.path.dirname(os.path.realpath(__file__))
nome = junta_nome(input('Digite nome do arquivo: '), local)

if verifica_se_existe(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as arq:
            file = [i.replace('\n', '').split(',') for i in arq.readlines()]
            file = [{'cidade': i[0],'hab': int(i[1])} for i in file ]
            maior = max(file, key= lambda cid: max(range(cid['hab'])))
            print(f'Cidade com maior numero de habitante: {maior["cidade"]}, total: {maior["hab"]}')
    except FileNotFoundError:
        print('Digite o nome do arquivo1')
else:
    print('Arquivo nao encontrado')