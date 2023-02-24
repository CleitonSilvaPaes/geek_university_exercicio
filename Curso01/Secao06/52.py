saque = int(input('Digite o Valor: '))
notas = [100, 50, 20, 10, 5, 2, 1]

for i in notas:
    print(f'Notas de {i}: {saque//i}')
    saque = saque % i