prova1 = float(input('Digite a nota da prova: '))
prova2 = float(input('Digite a nota da prova: '))
prova3 = float(input('Digite a nota da prova: '))

calc_media = ((prova1 * 1) + (prova2 * 1) + (prova3 * 2))/4

if calc_media >= 6:
    print('Aprovado')
else:
    print('Reprovado')