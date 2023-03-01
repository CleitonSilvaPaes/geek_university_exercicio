from random import randrange

# Montando o gabarito
gabarito = [['a', 'b', 'c', 'd', 'e'][randrange(5)]for i in range(10)]

# Adicionado alunos com suas notas e matriculas
alunos = {}
for i in range(3):
    alunos[i] = {
        'resp': [['a', 'b', 'c', 'd', 'e'][randrange(5)]for i in range(10)]
    }


# Verificar as resposta e atribuir nota
for chave, valor in alunos.items():
    nota = 0
    for resp in valor.values():
        for i in range(len(resp)):
            if gabarito[i] == resp[i]:
                nota += 1
    if nota >= 7:
        alunos[chave]['apt'] = True
    else:
        alunos[chave]['apt'] = False
    alunos[chave]['nota'] = nota

# Mostra se passou
for chave, valor in alunos.items():
    print(f'Matricula: {chave}')
    print('Respostas: ', *alunos[chave]['resp'])
    print(f'Nota: {alunos[chave]["nota"]}')
    print('Aprovado' if alunos[chave]["apt"] else 'Reprovado')
    print('Gabarito:  ', *gabarito)
    print()
