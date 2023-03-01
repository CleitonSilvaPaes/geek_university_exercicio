from random import randrange

alunos = [[['a', 'b', 'c', 'd'][randrange(4)] for i in range(10)] for j in range(5)]

respostas = [['a', 'b', 'c', 'd'][randrange(4)] for i in range(10)]

resultados = {}

for i in range(len(alunos)):
    pontos = 0
    for j in range(len(alunos[i])):
        nota = alunos[i][j]
        if nota == respostas[j]:
            # print(i, nota, respostas[j])
            pontos += 1
    resultados[f'aluno_{i + 1}'] = pontos

print(resultados)
