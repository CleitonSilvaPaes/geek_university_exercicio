from random import randint
num = randint(1, 1000)
rodar = True
count = 0
while rodar:
    chute = int(input('Digite seu chute: '))
    count+=1

    if chute > num:
        print('Maior')
    elif chute < num:
        print('Menor')
    else:
        print('Acertou')
        print(f'Tentativas: {count}')
        rodar = False