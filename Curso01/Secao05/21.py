opcao = int(input("""
Escolha a opcao
1 - Soma de 2 numeros
2 - Diferenca entre 2 numeros
3 - Produto entre 2 numeros
4 - Divisao entre 2 numeros

Opcao:
"""))

num1 = float(input('Digite numero 1°: '))
num2 = float(input('Digite numero 2°: '))

if opcao == 1:
    print(f'Soma: {num1 + num2}')

elif opcao == 2:
    if num2 > num1:
        num1, num2 = num2, num1
    print(f'Diferencao do maior pelo menor: {num1 - num2}')

elif opcao == 3:
    print(f'Produto: {num1 * num2}')

elif opcao == 4:
    if num2 != 0:
        print(f'Divisao: {num1 / num2}')
    else:
        print('Nao e possivel dividir por 0')
else:
    print('Opcao Invalida')