#! venv/Scripts/python
"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, nao podemos realizar a escrita nele. Da mesma forma, se abrimos um arquivo para escrita, nao podemos lelo, somente escrever nele.

Para escrevermos dados em um arquivo, apos abrir o arquivo utilizamos a funcao write() Esta funcao recebe uma string com parametro, caso contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo nao existir sera criado, caso ele ja exosta, o anterior sera apafado e um novo sera criado. Dessa forma, todo o conteudo no arquivo anterio e perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

with open('novo.txt', 'w') as arq:
    arq.write('Novos dados. \n')
    arq.write('Outros podemos colocar quantas linhas quisermos.\n')
    arq.write('Mais Esta e a ultima linha. \n')
    
"""
import os
os.system('cls')
dir_path = os.path.dirname(os.path.realpath(__file__))
localizar = dir_path + '\\texto.txt'

# Exemplo de escrita - modo 'w+' - escrita

with open(localizar, 'a', encoding='utf-8') as arq:
    print(arq.readlines())