from random import choice, randint
"""
lista = [
    {
        'sexo' = 'M' | 'F',
        'olhos' = 'A' | 'C',
        'cabelo' = 'L' | 'P' | 'C'
        'idade' = 0 | 100
    },
    
]
"""
def mostrar_dados(*args):
    for i in args:
        print(i)
        

def maior_idade(*args):
    maior = 0
    for i in args:
        if maior < i.get('idade'):
            maior = i.get('idade')
    return maior


def idade_media_olhos(*args):
    idade_soma = 0
    count = 0
    for i in args:
        if i.get('olho') == 'C' and i.get('cabelo') == 'P':
            idade_soma += i.get('idade')
            count += 1
    if count == 0:
        count = 1
    return idade_soma / count

def feminino_azuis_louros(*args):
    qtd = 0
    for i in args:
        if (i['sexo'] == 'F') and (i['idade'] >= 18 and i['idade'] <= 35) \
            and (i['olho'] == 'A' and i['cabelo'] == 'L'):
               qtd += 1
    return qtd
            

lista = [
    {
        'sexo': choice('MF'),
        'olho': choice('AC'),
        'cabelo': choice('LPC'),
        'idade': randint(0, 100)
    } for i in range(30)
]

# mostrar_dados(*lista)

print(f'Idade media das pessoas com olhos castanhos e cabelo preto: {idade_media_olhos(*lista):.0f}')
print(f'Maior idade entre os habitantes: {maior_idade(*lista)}')
print(f'Mulheres entre 18 a 35 com olhos azuis e cabelhos louros: {feminino_azuis_louros(*lista)}')