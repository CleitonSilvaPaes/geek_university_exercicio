hora_entrada = int(input('Digite a hora da entrada do veiculo: '))
minutos_entrada = int(input('Digite o minuto de entrada: '))
hora_saida = int(input('Digite a hora da saida do veiculo: '))
minutos_saida = int(input('Digite o minuto de saida: '))

DIA = 24

if hora_entrada >= 12 and hora_saida < 12:

    tmp = (minutos_entrada + minutos_saida)
    minutos_final = tmp % 60
    hora_final =  abs(hora_entrada - hora_saida - DIA) + tmp // 60
    hora_cobrada = hora_final

    if minutos_final > 0:

        hora_cobrada+=1

        if hora_final <= 2:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1}')

        elif hora_final <= 4:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1.4}')

        else:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 2}')

    elif hora_final <= 2:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1}')

    elif hora_final <= 4:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1.4}')

    else:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 2}')
else:

    tmp = (minutos_entrada + minutos_saida)
    minutos_final = tmp % 60
    hora_final =  abs(hora_entrada - hora_saida) + tmp // 60
    hora_cobrada = hora_final

    if minutos_final > 0:

        hora_cobrada+=1

        if hora_final <= 2:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1}')

        elif hora_final <= 4:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1.4}')

        else:

            print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 2}')

    elif hora_final <= 2:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1}')

    elif hora_final <= 4:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 1.4}')

    else:

        print(f'Horas: {hora_final}:{minutos_final} -- Valor a pagar {hora_cobrada * 2}')

