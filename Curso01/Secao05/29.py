from random import randint

acerto = 0

for i in range(5):
    
    a = randint(1, 100)
    b = randint(1, 100)
    
    print(f'Qual a soma dos numeros: {a} + {b} = ?')
    
    resposta = int(input('Digite a resposta: '))

    if resposta == (a + b):
        print('Acerto')
        acerto += 1
    else:
        print(f'Resposta correta: {a+b}')

print(f'Voce acertou {acerto}') 
