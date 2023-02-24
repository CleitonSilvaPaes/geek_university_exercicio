lado_a = float(input('Digite valor do 1° lado: '))
lado_b = float(input('Digite valor do 2° lado: '))
lado_c = float(input('Digite valor do 3° lado: '))

if (lado_a + lado_b) > lado_c \
    and (lado_a + lado_c) > lado_b \
    and (lado_c + lado_b) > lado_a:
    
    if lado_a == lado_b != lado_c or lado_a == lado_c != lado_b or lado_b == lado_c != lado_a:
        print('Isoceles')
    elif lado_a == lado_b == lado_c:
        print('Equilatero')
    else:
        print('Escaleno')
else:
    print('Valores não forma um triangulo')