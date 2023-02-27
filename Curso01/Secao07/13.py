import os

vetor = []

for i in range(1, 6):
    os.system('cls') or None

    x = float(input(f'Digite {i}°: '))
    vetor.append(x)
    
print(f'Maior: {max(vetor)}, Posicao: {vetor.index(max(vetor))+1}')
print(f'Menor: {min(vetor)}, Posicao: {vetor.index(min(vetor))+1}')
