import os
vetor = []

for i in range(1, 6):
    os.system('cls') or None

    x = float(input(f'Digite {i}°: '))
    vetor.append(x)
    
print(f'Todos os valores lido:', *vetor)
print(f'Maior: {max(vetor)}')
print(f'Menor: {min(vetor)}')
print(f'Media: {sum(vetor) / len(vetor)}')