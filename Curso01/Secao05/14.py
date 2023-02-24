nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))
nota3 = float(input('Digite uma nota: '))

calc_media_ponderada = ((nota1 * 2) + (nota2 + 3) + (nota3 * 5))/10

if 0 <= calc_media_ponderada <= 2.9:
    print('Reprovado')
elif 3 <= calc_media_ponderada <= 4.9:
    print('Recuperacao')
else:
    print('Aprovado')