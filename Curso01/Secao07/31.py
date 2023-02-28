from random import randrange
n = 10

vet1 = [randrange(1, 10) for i in range(n)]
vet2 = [randrange(1, 10) for i in range(n)]

vet3 = set(vet1).union(vet2)

print(f'Vetor1: ', * vet1)
print(f'Vetor2: ', * vet2)
print(f'A uniao dos vetores: ', *vet3)