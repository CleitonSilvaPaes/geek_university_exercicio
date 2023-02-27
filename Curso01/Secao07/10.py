notas = []

for i in range(15):
    x = float(input(f'Digite a nota {i+1}: '))
    notas.append(x)

print(f'Media Geral: {sum(notas)/len(notas)}')