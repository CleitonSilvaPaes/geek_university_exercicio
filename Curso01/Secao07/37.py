from random import randrange

n = 11

vet1 = [randrange(30) for i in range(n)]
vet1.sort()

tmp = (n // 2) + 1

troca = vet1[tmp:]
troca.sort(reverse=True)

print(vet1)
vet1[tmp:] = troca

print(vet1)