def data_por_extenco(*args):
    dia, mes, ano = args
    ano = str(ano)
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'marco',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro',
    }
    if meses.get(mes) is None:
        return 'Mes Invalido'
    elif( mes == 2 and (dia <= 0 or dia >= 28)) or (dia <= 0 or dia >= 31):
        return 'Dia Invalido'
    elif len(ano) != 4:
        return 'Ano invalido'
    return f'{dia} de {meses.get(mes)} de {ano}'

print(data_por_extenco(28, 3, 20))