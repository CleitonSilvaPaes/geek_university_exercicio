segundos = int(input('Digite um valor em segundos: '))

horas = segundos // 3600
tmp = segundos % 3600
minutos = tmp // 60
segundos = tmp % 60

print(f'Horas: {horas}:{minutos}:{segundos}')