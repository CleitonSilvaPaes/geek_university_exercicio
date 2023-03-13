import os
from time import sleep


def ler_arq(nome):
    file = []
    try:
        with open(nome, 'r') as arq:
            arq.seek(0)
            file = [i.replace('\n', '').split(',') for i in arq.readlines()]
            file = [{
                "matricula": i[0],
                "sobrenome": i[1],
                "ano_nacimento": i[2]
            } for i in file]
    except FileNotFoundError:
        with open(nome, 'x') as arq:
            pass
    return file


def salvar_arq(nome, file):
    with open(nome, 'w') as arq:
        arq.seek(0)
        for i in file:
            write = f'{i["matricula"]},{i["sobrenome"]},{i["ano_nacimento"]}\n'
            arq.write(write)


def isint(n):
    try:
        n = int(n)
        if n > 0:
            return n
        return 0
    except:
        return 0


def is_ano(n):
    if len(n) == 4:
        try:
            n = int(n)
            if n > 1990 and n < 2023:
                return n
            return 0
        except:
            return 0
    else:
        return 0
    
    
def is_sobrenome(n:str):
    return n.isalpha()


def cadastro_aluno(file:list):
    matricula = isint(input('Digite a matricula: '))
    sobrenome = input('Digite o sobrenome: ').split(' ')[0].title()
    ano = is_ano(input('Digite o ano de nacimento: '))
    if matricula and ano and is_sobrenome(sobrenome):
        if len(file) == 0:
            dado = {
                    "matricula": matricula,
                    "sobrenome": sobrenome,
                    "ano_nacimento": ano}
            file.append(dado)
            print('Cadastrado com sucesso')
        else:
            encontrou = False
            for i in file:
                if matricula == int(i["matricula"]) and encontrou == False:
                    print(f'Matricula ja cadastrada: {matricula}, nome: {i["sobrenome"]}')
                    encontrou = True
            if encontrou == False:
                dado = {
                    "matricula": matricula,
                    "sobrenome": sobrenome,
                    "ano_nacimento": ano}
                file.append(dado)
                print('Cadastrado com sucesso')
               


local = os.path.dirname(os.path.realpath(__file__))
nome = local+"\\alunos"

rodar = True
while rodar:
    file = ler_arq(nome)
    print('''
1 - Cadastrar Aluno
2 - Sair do programa''')
    op = input('Digite a opcao: ')
    if op == '1':
        cadastro_aluno(file)
        input()
    elif op == '2':
        rodar = False
    else:
        os.system('cls')
        print('Digite uma opcao valida!')
        sleep(1)
    salvar_arq(nome, file)