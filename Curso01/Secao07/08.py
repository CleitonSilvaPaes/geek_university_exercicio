vetor = []

for i in range(6):
    x = int(input(f'Digite {i+1}°: '))
    vetor.append(x)

print(f'Valores digitados na ordem inversa: ', *vetor[::-1])