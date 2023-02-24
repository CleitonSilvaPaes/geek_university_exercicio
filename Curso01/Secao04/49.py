horas = int(input('Digite um horario do inicio: '))
minutos = int(input('Digite um minuto do inicio: '))
segundos = int(input('Digite um segundo do inicio: '))
segundos_termino = int(input('Digite os segundos do termino: '))

# Converte os seguntos

horas_termino = segundos_termino // 3600
tmp = segundos_termino % 3600
minutos_termino = tmp // 60
segundos_termino = tmp % 60


# calculo para pegar os minustos da soma dos segundos

segundos_final = ((segundos + segundos_termino) % 60)
minutos_de_segundos_sobrando = (segundos + segundos_termino) // 60



# calculo para pegar as horas do minutos

minutos_final = ((minutos + minutos_termino + minutos_de_segundos_sobrando) % 60)
horas_de_minutos_sobrando = (minutos + minutos_termino + minutos_de_segundos_sobrando) // 60

# calcular a horas

hora_final = (horas + horas_termino + horas_de_minutos_sobrando)

print(f'Horario inical {horas}:{minutos}:{segundos}')
print(f'Horario final {hora_final}:{minutos_final}:{segundos_final}')


