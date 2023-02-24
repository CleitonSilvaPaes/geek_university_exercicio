soma = 0
count = 0

nota = int(input('Digite notas de 10 a 20: '))

while nota >= 10 and nota <=20:
    soma += nota
    count += 1
    nota = int(input('Digite notas de 10 a 20: '))

media = soma / count
print(f'Media: {media}')
    