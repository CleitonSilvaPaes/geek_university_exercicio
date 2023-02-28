from random import randrange

vetorA = [randrange(1,1000)for i in range(10)]
vetorB = [randrange(1,1000)for i in range(10)]
vetorC = []

pares = []
impares = []

vetorC.append(pares)
vetorC.append(impares)
for i in range(10):
    if vetorA[i] % 2 == 0:
        pares.append(vetorA[i])
    if vetorB[i] % 2 != 0:
        impares.append(vetorB[i])

for i in vetorC:
    print(i)