rodar = True
soma = 0
count = 1

while rodar:
    idade = int(input('Digite a idade: '))
    
    if idade != 0:
        soma += idade
        count +=1
    else:
        rodar = False
        print(f'Media da idade: {soma/count}')