vetor = set()
repetidos = set()
for i in range(1, 6):
    x = float(input(f'Digite {i}°: '))

    if x in vetor:
        print(f'Valor eliminado pois esta repetido: {x}')
        repetidos.add(x)
    vetor.add(x)

print(f'Valores eliminados: ', *repetidos)
print(f'Lista: {vetor}')