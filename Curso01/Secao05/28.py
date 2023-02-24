x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
z = float(input('Digite o valor de Z: '))

opcao = input("""
Opcao de Escolha:
(a) - Geometrica:
(b) - Ponderada:
(c) - Harmonica:
(d) - Aritmerica
""").lower()

if opcao == 'a':
    print(f'Geometrica: {(1/3)**(x*y*z)}')
elif opcao == 'b':
    print(f'Ponderada: {(x+2*y+3*z)/6}')
elif opcao == 'c':
    calc = (1/x) + (1/y) + (1/z)
    print(f'Harmonica: {1/calc}')
elif opcao == 'd':
    print(f'Aritmetrica: {(x + y + z)/3}')
else:
    print('Opcao invalida')

