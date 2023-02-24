carlos = float(input('Digite o salario: '))
joao = carlos/3

count = 0

rodar = True
while rodar:
    count += 1
    
    carlos = carlos + (carlos * 0.02)
    joao = joao + (joao * 0.05)

    if joao >= carlos:
        rodar = False
        print(f'Meses: {count}')
    
    