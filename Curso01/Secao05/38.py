ANO_ATUAL = 2018

data = input('Digite a data de nacimento (xx/xx/xxxx): ')

dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes > 0 and mes < 13:

    if mes == 1:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 2:

        if dia > 0 and dia < 30:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 3:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 4:

        if dia > 0 and dia < 31:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 5:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 6:

        if dia > 0 and dia < 31:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 7:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 8:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 9:

        if dia > 0 and dia < 31:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')
    
    elif mes == 10:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 11:

        if dia > 0 and dia < 31:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

    elif mes == 12:

        if dia > 0 and dia < 32:
            if ano <= ANO_ATUAL:
                print('data valida')
            else:
                print('data invalida')
        else:
                print('data invalida')

else:
    print('data invalida')