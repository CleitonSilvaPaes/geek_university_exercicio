from string import ascii_lowercase as letters
from io import StringIO
from random import choice, uniform, randint, seed

seed(0)

# Gerar os dados
file = []
for i in range(randint(10, 30)):
    alunos = {}
    alunos['nome'] = ''.join(choice(letters) for i in range(randint(5, 40)))
    alunos['nota'] = [round(uniform(0, 10), 2) for i in range(3)]
    if len(alunos['nome']) < 40:
        tamanho = 40 - len(alunos['nome'])
        alunos['nome'] += ''.join(' ' for i in range(tamanho))
    file.append(alunos)

# Arquivo Salvo
arq_original = StringIO()
for i in file:
    arq_original.write(f'{i["nome"]}, ')
    arq_original.write(f'{i["nota"][0]} {i["nota"][1]} {i["nota"][2]}')
    arq_original.write('\n')
arq_original.seek(0)

# Lendo o arqivo
with StringIO() as arq:
    file_arq = [i.replace('\n', '').split(',') for i in arq_original.readlines()]
    file_arq = [{"nome": i[0], "notas": sorted(list(map(float,  i[1].split())))} for i in file_arq]
    for i in file_arq:
        arq.write(f'{i["nome"]}, {i["notas"][0]} {i["notas"][1]} {i["notas"][2]} \n')
    arq.seek(0)
    print(arq.read())
    # [print(i) for i in file_arq]