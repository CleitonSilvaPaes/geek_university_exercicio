num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))
opcao = int(input("""
1 - Somar
2 - Subtrair
3 - Dividir
4 - Multiplicar
"""))

if opcao == 1:
    print(f'Valor da Soma: {num1 + num2}')
elif opcao == 2:
    print(f'Valor da Subtracao: {num1 - num2}')
elif opcao == 3:
    print(f'Valor da Divisao: {num1 / num2}')
elif opcao == 4:
    print(f'Valor da Multiplicacao: {num1 * num2}')
