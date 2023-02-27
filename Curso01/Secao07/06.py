
vetor = []

for i in range(10):
    x = int(input(f'Digite {i+1}°: '))
    vetor.append(x)

print(f'Maior numero digitado: {max(vetor)}')
print(f'Menor numero digitado: {min(vetor)}')