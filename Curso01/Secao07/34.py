vet = []

for i in range(10):
    rodar = True
    while rodar:
        x = float(input(f'Digite {i+1}: '))
        if x in vet:
            print('Numero já foi digitado')
        else:
            rodar = False
            vet.append(x)

print(f'Valores digitados: ', *vet)