data_valida = input('Digite uma data (xx/xx/xxxx): ').split('/')

dia, mes, ano = data_valida

dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes >= 1 and mes <= 12 and dia >=1 and dia <= 31:
    
    if mes == 2 and dia <= 29:
        print('valido')
    elif mes != 2:
        print('Valido')
    else:
        print('Invalido')

else:
    print('Invalido')