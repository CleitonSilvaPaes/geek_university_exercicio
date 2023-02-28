from random import randrange

n = 5

vet1 = [randrange(0, 15) for i in range(n)]

print(f'Vetor original: ', *vet1)
for i in vet1:
    if i == 0:
        vet1.remove(i)
     
print(f'Vetor: ', *vet1)