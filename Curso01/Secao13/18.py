from io import StringIO
import os


local = os.path.dirname(os.path.realpath(__file__))
nome = local+'\\compras'

with open(nome, 'r', encoding='utf-8') as arq:
    file = [(i.replace('\n', '').split(',')) for i in arq.readlines()]
    file = [{"produto": i[0],"valor": float(i[1])} for i in file]
    total = round(sum(list(map(lambda item: item["valor"], file))), 2)
    print(f'Total da compra: {total}, voce esta levando: {len(file)} produtos')