peso = float(input('Digite seu peso: '))
altura = int(input('Digite sua altura em cm (170): '))/100

imc = peso / (altura**2)

if imc <= 18.5:
    print('Abaixo do peso')
elif imc >= 18.6 and imc <= 24.9:
    print('Saudavel')
elif imc >= 25.0 and imc <= 29.9:
    print('Peso em excesso')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade Grau 1')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau 2(severa)')
else:
    print('Obesidade Grau 3(morbida)')
    