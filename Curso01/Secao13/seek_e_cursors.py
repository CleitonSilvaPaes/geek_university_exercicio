#! ../venv/Script
"""
Seek e Cursors

seek() -: E utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

# seek() -: A funcao seek() é utilizada para movimentacao do cursor pelo arquivo. ela recebe um parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a funcao seek()
arquivo.seek(22)

print(arquivo.read())

print(arquivo.readline()) # ler a primeira linha
print(arquivo.readline()) # segunda linha 

print(arquivo.readlines()) # le todas as linhas e transforma em list

# OBS: Quando abrimos um arquivo com a funcao open() é criada um conexao entre o arquivo no disco do computar e o nosso programa. Essa conecao é chanada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexao. Para isso utilizamos a funcao close()

Passos para se trabalhar com arquivo:

# 1 - Abrir o arquivo:
arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

# 3 - Fechar o arquivo
arquivo.close()
"""
import os

os.system('cls')


# 1 - Abrir o arquivo:
arquivo = open('texto.txt', encoding='utf-8')

# OBS: Se tentarmos manipular o arquivo apos seu fechamento, teremos um ValueError