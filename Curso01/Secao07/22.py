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
        valor = {'pos': i, 'par': vetorA[i]}
        pares.append(valor)
    if vetorB[i] % 2 != 0:
        valor = {'pos': i, 'impar': vetorB[i]}
        impares.append(valor)

for i in vetorC:
    for j in i:
        if j.get('par'):
            print(f'Posicao: {j.get("pos")}, Par: {j.get("par")}')
        else:
            print(f'Posicao: {j.get("pos")}, Impar: {j.get("impar")}')
