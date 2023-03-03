# This is a placeholder for correct code for this message.

def converter(horas: int, minutos: int, segundos: int) -> int:
    return (horas * 3600) + (minutos * 60) + (segundos)


horas = int(input('Digite a horas: '))
minutos = int(input('Digite a minutos: '))
segundos = int(input('Digite a segundos: '))

print(converter(horas, minutos, segundos))