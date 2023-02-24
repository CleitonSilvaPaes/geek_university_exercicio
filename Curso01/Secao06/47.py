rodar = True
while rodar:
    opcao = int(input("""
    1 - Adicao
    2 - Subtracao
    3 - Multiplicacao
    4 - Divisao
    5 - Sair: """))   
    
    if opcao != 5:
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            x = float(input('Digite: '))
            y = float(input('Digite: '))
            if opcao == 1:
                print(f'Soma: {x+y}')
            elif opcao == 2:
                print(f'Subtracao: {x-y}')
            elif opcao == 3:
                print(f'Multiplcacao: {x*y}')
            elif opcao == 4:
                if y != 0:
                    print(f'Divisao: {x/y}')
                else:
                    print('Imposivel divisao por 0')
        else:
            print('Opcao Invalida')
    else:
        rodar = False