import os
from time import sleep

def isfloat(n):
    try:
        n = float(n)
        if n >= 0 and n <= 10:
            return n
        return None
    except ValueError:
        return None


def ler_arq(nome):
    file = []
    try:
        with open(nome, 'r') as arq:
            arq.seek(0)
            file = [i.replace('\n', '').split(',') for i in arq.readlines()]
            file = [{
                "nome": i[0],
                "nota": float(i[1]),
            } for i in file]
    except FileNotFoundError:
        with open(nome, 'x') as arq:
            pass
    return file


def salvar_arq(nome, file:list):
    with open(nome, 'w') as arq:
        arq.seek(0)
        for i in file:
            write = f'{i["nome"]},{i["nota"]}\n'
            arq.write(write)


def informacoes_turma(file:list):
    notas = len(list(filter(lambda nt: nt>=7, [i["nota"] for i in file])))
    print(f'Total de alunos na turma: {len(file)}')
    aprovados = abs(round((notas/len(file) * 100), 2))
    reprovados = abs(round(100-aprovados, 2))
    print(f'Porcentagem de alunos aprovados: {aprovados}%')
    print(f'Porcentagem de alunos reprovados: {reprovados}%')
    input()


def inserir_aluno(file:list):
    nome = input('Digite o nome do aluno: ')
    nota = isfloat(input('Digite a nota do aluno: '))
    if nota:
        dado = {
                "nome": nome,
                "nota": nota,
                }
        file.append(dado)
    else:
        print('Digite uma nota valida de 0 a 10')
    input()
        

def exibir_media_alunos(file:list):
    notas = sum([i["nota"] for i in file])
    print(f'Media dos alunos: {round(notas/len(file), 2)}')
    input()


def exibir_aprovados(file:list):
    alunos = list(map(lambda nt: nt, filter(lambda nt: nt["nota"]>=7, [i for i in file])))
    alunos = sorted(alunos, key=lambda nt: nt["nota"], reverse=True)
    print("Alunos aprovados")
    [print(f'Nome: {i["nome"].title()}, Nota: {i["nota"]}') for i in alunos]
    input()


def exibir_reprovados(file:list):
    alunos = list(map(lambda nt: nt, filter(lambda nt: nt["nota"]< 7, [i for i in file])))
    alunos = sorted(alunos, key=lambda nt: nt["nota"], reverse=True)
    print("Alunos Reprovados")
    [print(f'Nome: {i["nome"].title()}, Nota: {i["nota"]}') for i in alunos]
    input()


local = os.path.dirname(os.path.realpath(__file__))
nome = local+"\\alunos_"
file = ler_arq(nome)

rodar = True
while rodar:
    os.system('cls')
    print("""
1 - Informacoes da turma
2 - Inserir aluno e nota
3 - Exibir medias dos alunos
4 - Exibir alunos aprovados
5 - Exibir alunos reprovados
6 - Salvar dados em disco
0 -  Sair do progrma         
""")
    op = input('Digite a opcao: ')
    
    if op == '0':
        rodar = False
    elif op == '1':
        informacoes_turma(file)
    elif op == '2':
        inserir_aluno(file)
    elif op == '3':
        exibir_media_alunos(file)
    elif op == '4':
        exibir_aprovados(file)
    elif op == '5':
        exibir_reprovados(file)
    elif op == '6':
        salvar_arq(nome, file)
    else:
        print('Opcao invalida!')
    sleep(.5)