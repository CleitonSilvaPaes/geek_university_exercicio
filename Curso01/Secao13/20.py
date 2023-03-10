from string import ascii_lowercase as letter
from random import choice, randint, uniform
from io import StringIO


def isint(n):
    try:
        n = int(n)
        return n
    except BaseException as err:
        return 0


n_alunos = isint(input('Digite o numero de alunos: '))
if n_alunos > 0:
    # Gerar dados
    alunos = []
    notas = [round(uniform(0, 10), 2) for i in range(n_alunos)]
    for i in range(n_alunos):
        text = ''.join(choice(letter) for j in range(randint(5, 40)))
        if len(text) < 40:
            calc = 40 - len(text)
            text += ''.join(' ' for j in range(calc))
        alunos.append(text.title())
    with StringIO() as arq:
        for i in range(n_alunos):
            arq.write(f'{alunos[i]}, {notas[i]}\n')
        arq.seek(0)
        print(arq.read())
else:
    print('Digite um numero valido!')