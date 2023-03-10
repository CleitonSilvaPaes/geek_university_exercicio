from string import ascii_letters as letter
from random import choice, randint, uniform
from io import StringIO

# Gerar dados para o arquivo alunos_notas
alunos_notas = [{
    "nome": ''.join(choice(letter) for _ in range(randint(5, 15))).title(),
    "nota": float(round(uniform(0, 10),2 ))} for i in range(30)]

# Gravando no arquivo
notas_alunos = StringIO()
for i in alunos_notas:
    notas_alunos.write(f'{i["nome"]}, {i["nota"]}\n')
notas_alunos.seek(0)

# Lendo o arquivo
with notas_alunos as arq:
    file = [(i.replace('\n', '').replace(',', '').split()) for i in arq.readlines()]
    maior_nota = max(file, key=lambda alunos: alunos[1])
    print(f'Aluno com a maior nota: {maior_nota[0]}, nota: {maior_nota[1]}')