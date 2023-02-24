altura = int(input('Digite sua altura cm: '))
peso = float(input('Digite seu peso: '))

if altura <= 120:
    if peso <= 60:
        print('A')
    elif peso >= 60 and peso <= 90:
        print('D')
    elif peso > 90:
        print('G')
elif altura >= 121 and altura <= 170:
    if peso <= 60:
        print('B')
    elif peso >= 60 and peso <= 90:
        print('E')
    elif peso > 90:
        print('H')
elif altura > 170:
    if peso <= 60:
        print('C')
    elif peso >= 60 and peso <= 90:
        print('F')
    elif peso > 90:
        print('I')