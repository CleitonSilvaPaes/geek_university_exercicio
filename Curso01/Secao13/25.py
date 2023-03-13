import os
import re


def isint(n):
    try:
        n = int(n)
        return n
    except: 
        return None


def ler_arq(nome):
    file = []
    try:
        with open(nome, 'r') as arq:
            arq.seek(0)
            file = [i.replace('\n', '').split(',') for i in arq.readlines()]
            file = [{
                "nome": i[0],
                "tel": i[1],
                "ani": i[2]
            } for i in file]
    except FileNotFoundError:
        with open(nome, 'x') as arq:
            pass
    return file


def salvar_arq(nome, file):
    with open(nome, 'wb') as arq:
        arq.seek(0)
        for i in file:
            write = f'{i["nome"]},{i["tel"]},{i["ani"]}\n'.encode()
            arq.write(write)


def inserir_contato(file):
    nome_contato = input('Digite o nome: ')
    check_tel = re.compile('(\(?\d{2}\)?\s)?(\d{4,5}?\d{4})')
    check_ani = re.compile('^(0[1-9]|[12][0-9]|3[01]) (0[1-9]|1[012])')
    telefone = input('Digite o numero de telefone: ')
    aniversario = input('Digite (dia e mes) de aniversario separado por espaco: ')
    if check_tel.match(telefone) and check_ani.match(aniversario):
        if len(file) == 0:
            dado = {
                "nome" : nome_contato.title(),
                "tel": telefone,
                "ani": aniversario}
            file.append(dado)
            print('Contato cadastrado com Sucesso')
        else:
            encontrou = False
            for i in file:
                if telefone == i["tel"] and encontrou == False:
                    encontrou = True
                    print(f'Telefone ja cadastrado como usuario: {i["nome"]}')
            if encontrou == False:
                dado = {
                "nome" : nome_contato.title(),
                "tel": telefone,
                "ani": aniversario}
                file.append(dado)
            print('Contato cadastrado com Sucesso')    
    else:
        print(f'Telefone ou aniversario invalido!')


def remover_contato(file):
    if len(file) == 0:
        print('Lista de contato vazia')
    else:
        for index, item in enumerate(file):
            print(f'Opcao: {index} - Nome: {item["nome"]}, Telefone: {item["tel"]}, Aniversario: {item["ani"]}')
        op = isint(input('Digite a opcao para remover: '))
        if op != None:
            try:
                file.pop(op)
                print('Removido com sucesso')
            except IndexError:
                print('Digite uma opcao valida')
        else:
            print('Digite uma opcao valida')
            

def pequisar_contato_pelo_nome(file):
    if len(file) == 0:
        print('Lista de contato vazia')
    else:
        contatos = []
        nome_contato = input('Digite o nome do contato: ')
        for i in file:
            if nome_contato.title() == i["nome"]:
                contatos.append(i)
        if len(contatos) != 0:
            for index, item in enumerate(contatos):
                print(f"{index+1} -> Nome: {item['nome']}, Telefone: {item['tel']}, Aniversario: {item['ani']}")
        else:
            print('Contato nao incontrado')


def listar_todos_contatos(file):
    if len(file) == 0:
        print('Lista de contato vazia')
    else:
        for index, item in enumerate(file):
            print(f"{index+1} -> Nome: {item['nome']}, Telefone: {item['tel']}, Aniversario: {item['ani']}")
            

def lista_contato_pela_letra(file):
    if len(file) == 0:
        print('Lista de contato vazia')
    else:
        contatos = []
        nome_contato = input('Digite a letra do contato: ')
        for i in file:
            if nome_contato.title()[0] == i["nome"][0]:
                contatos.append(i)
        if len(contatos) != 0:
            for index, item in enumerate(contatos):
                print(f"{index+1} -> Nome: {item['nome']}, Telefone: {item['tel']}, Aniversario: {item['ani']}")
        else:
            print('Contato nao incontrado')


def mostrar_aniversariante(file):
    if len(file) == 0:
        print('Lista de contato vazia')
    else:
        contatos = []
        mes = input('Digite a mes: ')
        for i in file:
            if mes == i["ani"].split()[1]:
                contatos.append(i)
        if len(contatos) != 0:
            for index, item in enumerate(contatos):
                print(f"{index+1} -> Nome: {item['nome']}, Telefone: {item['tel']}, Aniversario: {item['ani']}")
        else:
            print('Nao tem aniversariante esse mes')


local = os.path.dirname(os.path.realpath(__file__))
nome = local+"\\agenda"

rodar = True
while rodar:
    file = ler_arq(nome)
    os.system('cls')
    print("""
1 - inserir contato
2 - remover contato
3 - perquisar um contato pelo nome
4 - listar todos os contatos
5 - perquisar o contato pela letra
6 - mostra os aniversariantes do mes
0 - sair do programa          
""")
    op = input('Digite sua opcao: ')
    if op == '1':
        inserir_contato(file)
        input()
    elif op == '2':
        remover_contato(file)
        input()
    elif op == '3':
        pequisar_contato_pelo_nome(file)
        input()
    elif op == '4':
        listar_todos_contatos(file)
        input()
    elif op == '5':
        lista_contato_pela_letra(file)
        input()
    elif op == '6':
        mostrar_aniversariante(file)
        input()
    elif op == '0':
        rodar = False
    else:
        print('Digite uma opcao valida!')
    salvar_arq(nome, file)