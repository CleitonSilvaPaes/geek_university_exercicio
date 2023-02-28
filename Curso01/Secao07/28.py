from random import randrange

vetorA = []
vetorB = []
vetorC = []

pares = []
impares = []

vetorC.append(pares)
vetorC.append(impares)
for i in range(3):
    x = int(input(f'Digite numero {i+1}: '))
    if x % 2 == 0:
        valor = {'par': x}
        pares.append(valor)
    if x % 2 != 0:
        valor = {'impar': x}
        impares.append(valor)

print('UTILIZADOS: ')
for i in vetorC:
    for j in i:
        if j.get('par'):
            print(f'{j.get("par")}', end=' ')
        else:
            print(f'{j.get("impar")}', end=' ')

# for i in vetorC:
#     for j in i:
#         if j.get('par'):
#             print(f'UTILIZADOS Par: {j.get("par")}')
#         else:
#             print(f'UTILIZADOS Impar: {j.get("impar")}')