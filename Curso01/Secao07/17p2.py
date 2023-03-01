from random import random

n_alunos, n_provas = 10, 3

# montar as notas
notas_alunos = [[round(random() * 10, 1) for i in range(n_provas)] for j in range(n_alunos)]

# controle das notas
contabilizar = {
    'prova0': {},
    'prova1': {},
    'prova2': {},
}

# Verifica as notas e o aluno
for i in range(n_provas):
    for j in range(n_alunos):
        if contabilizar[f'prova{i}'].get('nota') == None:
            contabilizar[f'prova{i}']['nota'] = notas_alunos[j][i]
            contabilizar[f'prova{i}']['aluno'] = j
        elif contabilizar[f'prova{i}']['nota'] >= notas_alunos[j][i]:
            contabilizar[f'prova{i}']['nota'] = notas_alunos[j][i]
            contabilizar[f'prova{i}']['aluno'] = j

# Apresenta para o usuario
for index, (_, aluno) in enumerate(contabilizar.items()):
    print(f'Prova: {index}')
    print(f'Nota: {aluno["nota"]}')
    print(f'Aluno: {aluno["aluno"]}')
    print()
