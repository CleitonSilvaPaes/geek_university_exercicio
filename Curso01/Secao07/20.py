vetor = []
vetor2 = []

for i in range(1, 7):
    rodar = True
    while rodar:
        x = int(input(f'Digite {i}: '))
        if x >= 0 and x <= 50:
            rodar = False
            vetor.append(x)
            if x % 2 != 0:
                vetor2.append(x)

print('Vetor Original')
for i in range(0, len(vetor), 2):
    print(vetor[i], vetor[i+1])

print('Vetor de Impares')
for i in range(0, len(vetor2), 2):
    if len(vetor2) % 2 != 0:
        if i < len(vetor2)-1:
            print(vetor2[i], vetor2[i+1])
        else:
            print(vetor2[i])
    else:
        print(vetor2[i], vetor2[i+1])
