vetor = []

for i in range(10):
    x = float(input(f'Digite {i+1}°: '))
    vetor.append(x)

print(f'Maior numero digitado {max(vetor)}')
print(f'Posicao que se encontra {vetor.index(max(vetor))+1}')