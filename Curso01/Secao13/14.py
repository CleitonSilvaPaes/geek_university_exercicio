import os 
from io import StringIO
import datetime

local = os.path.dirname(os.path.realpath(__file__))
nome = local+'\\nome_e_data'

data = datetime.date.today().year

with open(nome, encoding='UTF-8') as arq:
    file = [(i.replace('\n','').split(',')) for i in arq.readlines()]
    file = [{'nome' : i[0], 'data' : i[1]} for i in file]
    with StringIO('') as arq_save:
        texto = (list(map(lambda file: f'{file["nome"]}, {data - int(file["data"].split()[2])}', file)))
        for i in texto:
            arq_save.write(f'{i}\n')
        arq_save.seek(0)
        print(arq_save.read())