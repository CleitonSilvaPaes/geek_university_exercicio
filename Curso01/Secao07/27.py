vet = []
pos = []

for i in range(10):
    x = int(input(f"Digite {i+1}: "))
    vet.append(x)
    if x % 2 != 0:
        valor = {'pos': i, 'valor': x}
        pos.append(valor)

print(f'Vetor: {vet}')
for i in pos:
    print(f'Posicao: {i.get("pos")}, Valor Impar: {i.get("valor")}')
