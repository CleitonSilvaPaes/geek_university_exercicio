import os
from io import StringIO

def junta_nome(nome, local):
    return local + f'\\{nome}'


def verifica_arquivo_data(file):
   try:
       [int(i[1].split()[2]) for i in file if len(i[1].split()[2]) == 4]
       return True
   except IndexError as err:
       return False
       

def verificar_data(data):
    if len(data) == 4:
        try:
            data = int(data)
            return True
        except BaseException as err:
            return False
    return False
       
local = os.path.dirname(os.path.realpath(__file__))
nome = junta_nome(input('Digite o nome de arquivo: '), local)
try:
    with open(nome, encoding='UTF-8') as arq:
        file = [i.replace('\n', '').split(',') for i in arq.readlines()]
        if verifica_arquivo_data(file):
            ano = input('Digite o ano atual: ')
            maior = int(max(file, key=lambda file: file[1].split()[2])[1].split()[2])
            if verificar_data(ano) and (int(ano) >= maior):
                ano = int(ano)
                with StringIO('') as arq_save:
                    nome = ''
                    for i in file:
                        nome = i[0]
                        idade = ano - int(i[1].split()[2])
                        if idade >= 0 and idade <= 100:
                            if idade > 18:
                                arq_save.write(f'{nome}, maior de idade\n')
                            elif idade < 18:
                                arq_save.write(f'{nome}, menor de idade\n')
                            else:
                                arq_save.write(f'{nome}, entrando na maior\n')
                    arq_save.seek(0)
                    print(arq_save.read())
            else:
                print(f'Data invalida formato (xxxx) e maior: {maior}')
        else:
            print('Arquivo Invalido para conversao de data')
except FileNotFoundError:
    print('Arquivo nao encontrado!')