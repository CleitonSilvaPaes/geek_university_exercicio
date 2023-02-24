comprimento = float(input('Digite o comprimento do terreno: '))
largura = float(input('Digite o largura do terreno: '))
tela = float(input('Digite o custo do metro da tela: '))

preco_total = ((comprimento + largura) * 2) * tela 

print(f'Valor ficaria: {preco_total}')