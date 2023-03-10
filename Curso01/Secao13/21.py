from string import ascii_lowercase as letter
from random import choice, randint, uniform
from io import StringIO
import os 

local = os.path.dirname(os.path.realpath(__file__))
nome = local+"\\text.bin"

with open(nome, 'rb') as arq:
    file = [(i.decode().replace('\n', '').split(',')) for i in arq.readlines()]
    maior = max(file, key=lambda notas: notas[1])
    print(f'Aluno com a maior nota: {maior[0]}, nota: {maior[1]}')