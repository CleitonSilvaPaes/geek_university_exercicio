import os


def verifica_se_existe(nome:str): 
    if os.path.exists(nome):
        return True
    return False


def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


local = os.path.dirname(os.path.realpath(__file__))
nome_do_arquivo1 = junta_nome(input('Digite o nome do 1° arquivo: '), local)

if verifica_se_existe(nome_do_arquivo1):
    try:
        with open(nome_do_arquivo1, 'r', encoding='utf-8') as arq1:
            palavra = input('Digite a palavra que deseja contar: ')
            texto = [ i.replace('\n','').replace(',', '').replace('.','').split() for i in arq1.readlines() if len(i.split()) != 0]
            count = 0
            for i in texto:
                for j in range(len(i)):
                    if i[j] == palavra:
                        print(i[j], j)
                        count+=1
            if count != 0:
                print(f'Foi encontra: {palavra} :{count} vezes.')
            else:
                print('Infelizmente nao foi encontrado ')
    except FileNotFoundError:
        print('Digite o nome do arquivos')
else:
    print('Arquivos nao encontrado')