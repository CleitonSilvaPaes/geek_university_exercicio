numero = int(input('Digite um numero: '))

if numero <= 0:
    print('Numero invalido')
else:
    soma = 0
    numero = str(numero)
    
    for i in numero:
        soma += int(i)
    print(f'Soma dos numeros: {soma}')