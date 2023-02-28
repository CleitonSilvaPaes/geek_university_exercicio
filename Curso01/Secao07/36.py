from random import randrange

n =10

vet1 = [randrange(30) for i in range(n)]

print(f'Vetor orginal: ', *vet1)
print(f'Vetor Ordenado: ', *sorted(vet1))