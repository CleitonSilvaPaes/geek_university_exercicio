import os
from time import sleep


def isint(n):
    try:
        n = int(n)
        if n > 0:
            return n
        return 0
    except:
        return 0
    

def ler_arq(nome):
    file = []
    with open(nome, 'rb') as arq:
        arq.seek(0)
        file = [i.decode().replace('\n', '').split(',') for i in arq.readlines()]
    return file


def cadastrar_produto(nome):
    file = ler_arq(nome)
    cod = isint(input('Digite o codigo do produto: '))
    qtd = isint(input('Digite a quantidade: '))
    
    if cod and qtd:
        if len(file) == 0:
            desc = input('Digite a descricao do produto: ')
            if len(desc) > 0:
                dado = {"cod": cod, "desc": desc, "qtd": qtd}
                file.append(dado)
                print('Cadastrado com sucesso')
            else:
                print('Descricao tem que ter mais caracter!')
        else:
            file = [{
                "cod": int(i[0]),
                "desc": i[1],
                "qtd": int(i[2])} for i in file]
            encontou = False
            for i in range(len(file)):
                if file[i]["cod"] == cod and encontou == False:
                    file[i]["qtd"] += qtd
                    encontou = True
                    print('Cadastrado com sucesso')
            if encontou == False:
                desc = input('Digite a descricao do produto: ')
                if len(desc) > 0:
                    dado = {"cod": cod, "desc": desc, "qtd": qtd}
                    file.append(dado)
                    print('Cadastrado com sucesso')
                else:
                    print('Descricao tem que ter mais caracter!')
                    
    else:
        print('Codigo ou Quatidade está incorreto')
    with open(nome, 'wb') as arq:
        arq.seek(0)
        for i in file:
            write = f'{i["cod"]},{i["desc"]},{i["qtd"]}\n'.encode()
            arq.write(write)
                

def retirar_produto(nome):
    file = ler_arq(nome)
    
    if len(file) != 0:
        file = [{
                "cod": int(i[0]),
                "desc": i[1],
                "qtd": int(i[2])} for i in file]
        cod = isint(input('Digite o codigo do produto: '))
        qtd = isint(input('Digite a quantidade: '))
        if cod and qtd:
            encontou = False
            for i in range(len(file)):
                if file[i]["cod"] == cod and file[i]["qtd"] >= qtd and encontou == False:
                    file[i]["qtd"] -= qtd
                    encontou = True
                    print('Removido com sucesso')
                elif qtd > file[i]["qtd"]:
                    print('Quantidade maior que o permitido!')
            if encontou == False:
                print('Produto nao cadastrado')
            pass
        else:
            print('Codigo ou Quatidade está incorreto')

    else:
        print('Nao ha produto cadastrado')
    with open(nome, 'wb') as arq:
        arq.seek(0)
        for i in file:
            write = f'{i["cod"]},{i["desc"]},{i["qtd"]}\n'.encode()
            arq.write(write)
    

def relatorio(nome):
    file = ler_arq(nome)
    if len(file) != 0:
        print(f'Total de produtos: {len(file)}')
        print('-' * 60)
        for i in file:
            print(f'Codigo: {i[0]}')
            print(f'Descricao: {i[1]}')
            print(f'Quantidade: {i[2]}')
        print('-' * 60)
        input()
    else:
        print('Nao ha produto cadastrado')


def relatorio_produto_indiponivel(nome):
    file = ler_arq(nome)
    if len(file) != 0:
        faltante = []
        for i in file:
            if int(i[2]) == 0:
                faltante.append(i)
        print(f'Total de produtos: {len(faltante)} zerado no estoque')
        for i in faltante:
            print(f'Codigo: {i[0]}')
            print(f'Descricao: {i[1]}')
            print(f'Quantidade: {i[2]}')
        print('-' * 60)
        input()

    else:
        print('Nao ha produto cadastrado')
    input()
        


local = os.path.dirname(os.path.realpath(__file__))
nome = local+'\\controle'

rodar = True
while rodar:
    os.system('cls')
    print("""
1 - Cadastrar Produto
2 - Retirar Produto
3 - Relatorio Gerar
4 - Relatorio de produtos nao disponivel
0 - Sair
""")
    opcao = input('Digite uma das opcao: ')
    if opcao == '1':
        cadastrar_produto(nome)
    elif opcao == '2':
        retirar_produto(nome)
    elif opcao == '3':
        relatorio(nome)
    elif opcao == '4':
        relatorio_produto_indiponivel(nome)
    elif opcao == '0':
        rodar = False
    else:
        os.system('cls')
        print('Digite uma opcao valida')
    sleep(1)