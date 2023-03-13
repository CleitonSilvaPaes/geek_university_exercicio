import os 

def isint(n):
    try:
        n = int(n)
        if n > 0:
            return n
        return  0
    except:
        return 0


def verifica_proficao(*args):
    valid = []
    for i in args:
        if i.isalpha():
            valid.append(i)
        else:
               valid.append(None)
    return valid if None not in valid else []


local = os.path.dirname(os.path.realpath(__file__))
nome_arquivo = local+"\\emp.txt"

for i in range(5):
    rodar = True
    while rodar:
        profissao = input(f'Digite a profissao do {i+1}° funcionario: ')
        if verifica_proficao(*profissao.split()):
            tempo = isint(input(f'Digite a tempo de servico do {i+1}° funcionario em anos: '))
            if tempo:
                rodar = False
                with open(nome_arquivo, 'a', encoding='utf-8') as arq:
                    arq.write(f"{profissao.title()}, {tempo} \n")
            else:
                print(f'Tempo de servico tem que ser maior que 0')
        else:
            print('A proficao tem que ser somente letras')