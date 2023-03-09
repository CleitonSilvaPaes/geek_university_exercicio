import os
import re

def junta_nome(nome:str, local:str):
    return local + f'\\{nome}'


local = os.path.dirname(os.path.realpath(__file__))
nome = junta_nome(input('Digite o nome arquivo: '), local)

try:
    with open(nome, 'a', encoding='utf-8') as arq:
        rodar = True
        while rodar:
            nome = input('Digite nome: ')
            if len(nome) != 0:
                tel = input('Digite o telefone: ')
                check = re.compile('(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})')
                if tel != '0':
                    if check.match(tel):
                        arq.write(f'{nome},{tel}')
                    else:
                        print('Digite um numero valido!')
                else:
                    rodar = False
            else:
                'Digite um nome valido'
except Exception:
    pass