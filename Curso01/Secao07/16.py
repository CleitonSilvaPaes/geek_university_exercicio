vetor = []

for i in range(1, 6):
    x = float(input(f'Digite {i}: '))
    vetor.append(x)

cod = int(input("""
1 - Mostrar na ordem digitada
2 - Ordem Inversa
0 - Sair
"""))

resposta = {
    1: vetor,
    2: vetor[::-1],
    0: 'ate mais'
}

if resposta.get(cod) == None:
    print(f'Codigo Invalido')
else:
    print(*resposta.get(cod))