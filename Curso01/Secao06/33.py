n = int(input("Digite o 1° numero: "))
i = int(input('Digite o 2° numero: '))
j = int(input('Digite o 3° numero: '))

saida = '0'
count = 0 
if i != 0 and j != 0:
    num = 1
    while count != n-1:
        if num % i == 0 or num % j == 0:
            saida += f', {num}'
            count +=1
        num += 1
    saida +='.'
print(f'Saida: {saida}')

