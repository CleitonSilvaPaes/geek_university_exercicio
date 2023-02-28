conjunto = []

maior = 0
cod1 = 0
menor = 0
cod2 = 0

for i in range(10):
    rodar = True
    while rodar:
        cod = int(input(f'Digite o codigo do aluno {i+1}: '))
        altura = int(input(f'Digite a altura do aluno {i+1}: '))

        if len(conjunto) != 0:
            for j in range(len(conjunto)):
                if cod == conjunto[j][0]:
                    print('Codigo ja existente!')
                else:
                    rodar = False
                    conjunto.append((cod, altura))
                    if altura > maior:
                        maior = altura
                        cod1 = cod
                    if altura < menor:
                        menor = altura
                        cod2 = cod
        else:
            conjunto.append((cod, altura))
            maior, menor = altura, altura
            cod1, cod2 = cod, cod
            rodar = False

print(f'Aluno: {cod1} é o maior {maior} da turma')
print(f'Aluno: {cod2} é o menor {menor} da turma')
