"""
O bloco with 

Passo para se trabalhat com arquivos

# 1 - Abrimos o arquivo
# 2 - Manupulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados sao fechados apos o bloco with
"""
import os
os.system('cls')

location = os.path.abspath('texto.txt')

# O bloco with - Forma Pythonica de manipular arquivos

with open(location, encoding='utf-8') as arq:
    print(arq.read()) 
