import os
from time import sleep

def isint(n):
    try:
        n = int(n)
        if n > 0:
            return True
        return False
    except ValueError as err:
        return False


def ismes(n):
    try:
        n = int(n)
        if n >= 1 and n <= 12:
            return True
        return False
    except ValueError:
        return False


def isfloat(n):
    try:
        n = float(n)
        if n >= 0:
            return True
        return False
    except ValueError:
        return False


def criar_arq(nome):
    try:
        with open(nome, 'x') as arq:
            print('Arquivo criado com sucesso!')
    except FileExistsError:
        print('Arquivo ja existe')


def ler_arq(nome):
    file = []
    try:
        with open(nome, 'r') as arq:
            arq.seek(0)
            file = [i.replace('\n', '').split(',') for i in arq.readlines()]
            file = [{
                "cod": i[0],
                "nome": i[1],
                "venda": i[2],
                "mes": i[3]
            } for i in file]
    except FileNotFoundError:
        print('Arquivo ainda nao foi criado mas pode manipular os dado somente salvar que nao')
    return file


def salvar_arq(nome, file:list):
    if os.path.exists(nome):
        with open(nome, 'w') as arq:
            arq.seek(0)
            for i in file:
                write = f'{i["cod"]},{i["nome"]},{i["venda"]},{i["mes"]}\n'
                arq.write(write)
        return True
    else:
        return False


def inserir_registro(file:list):
    cod = input('Digite o codigo do vendedor: ')
    if isint(cod):
        nome = input('Digite o nome do vendedor: ')
        venda = input('Digite o valor da venda: ')
        mes = input('Digite o mes: ')
        if isfloat(venda) and ismes(mes) and nome.isalpha():
            dado = {
                "cod": cod,
                "nome": nome.title(),
                "venda": venda,
                "mes": mes
            }
            if len(file) > 0:
                encontrou = False
                for i in file:
                    if cod == i["cod"] and mes == i["mes"]:
                        encontrou = True
                if encontrou == False:
                    file.append(dado)
                    print('Cadastrado com sucesso')
                else:
                    print('Falha ao cadastrar pois essa venda ja foi cadastrada')
            else:
                file.append(dado)
                print('Cadastrado com sucesso')
                
        else:
            print('Digite valores valido para o cadastro')
    else:
        print('Codigo invalido!')


def excluir_registro(file:list):
    if len(file) > 0:
        mostrar_registros(file)
        op = input('Digite a opcao: ')
        if isint(op):
            try:
                op = int(op)
                file.pop(op-1)
                print('Removido com sucesso')
            except IndexError as err:
                print('Digite uma opcao valida!')

        else:
            print('Digite uma opcao valida!')
    else:
        print('Cadastre primeiro para poder excluir')


def alterar_valor_venda(file:list):
    if len(file) > 0:
        mostrar_registros(file)
        op = input('Digite a opcao: ')
        if isint(op):
            valor = input('Digite o valor: ')
            if isfloat(valor):
                op = int(op)
                print(file[op-1]["venda"])
                file[op-1]["venda"] = valor
                print('Alterado com sucesso')
            else:
                print('Digite um valor valido')
        else:
            print('Digite uma opcao valida!')
    else:
        print('Cadastre primeiro para poder alterar')


def mostrar_registros(file:list):
    if len(file) > 0:
        for index, item in enumerate(file):
            print(f'{index+1} -: Cod: {item["cod"]}, Nome: {item["nome"]}, venda: {item["venda"]}, Mes: {item["mes"]}')
    else:
        print('Cadastre primeiro para poder mostrar os cadastro')


def excluir_arq(nome):
    if os.path.exists(nome):
        os.remove(nome)
        print('Removido com sucesso')
    else:
        print('Arquivo nao exite!')

local = os.path.dirname(os.path.realpath(__file__))
nome = local + "\\vendedores"
file = ler_arq(nome)

rodar = True
while rodar:
    os.system('cls')
    print('''
1 - Criar o arquivo para salvar dados
2 - Incluir registro no arquivo
3 - Excluir registro no arquivo
4 - Alterar o valor de uma venda no arquivo
5 - Mostrar todos os registo
6 - Excluir arquivo
0 - Finaliza o programa e salva
''')
    op = input('Digite uma das opcao acima: ')
    if op == '0':
        if salvar_arq(nome, file):
            rodar = False
        else:
            print('Deseja sair sem salva?')
            escolha = input('Sim ou Nao, digite S/N qualquer letra diferente sera considerado N: ').lower()
            if len(escolha) > 0 and escolha[0] == 's':
                rodar = False
            else:
                pass
    elif op == '1':
        criar_arq(nome)
        input()
    elif op == '2':
        inserir_registro(file)
        input()
    elif op == '3':
        excluir_registro(file)
        input()
    elif op == '4':
        alterar_valor_venda(file)
        input()
    elif op == '5':
        mostrar_registros(file)
        input()
    elif op == '6':
        print('Tem certeza que deseja excluir')
        escolha = input('Digite S ou N: ').lower()
        if len(escolha) > 0 and escolha[0] == 's':
            excluir_arq(nome)
        else:
            print('Digite uma opcao valida!')
    else:
        print('Digite uma opcao valida!')
    sleep(1)