vetor = set()

for i in range(1, 11):
    x = float(input(f'Digite {i}°: '))

    if x in vetor:
        print(f'Valor já estava adicionado: {x}')
    vetor.add(x)