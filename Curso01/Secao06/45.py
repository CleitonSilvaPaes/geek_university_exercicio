rodar = True
while rodar:
    opcao = int(input("""
    1 - converter Km/h para m/s
    2 - converter m/s para Km/h
    0 - para sair do programa: """))   
    
    if opcao != 0:
        x = float(input('Digite: '))
        if opcao == 1:
            print(f'Metros: {x*1000}')
        elif opcao == 2:
            print(f'Km/s: {x/1000}')
        else:
            print('Opcao Invalida')
    else:
        rodar = False