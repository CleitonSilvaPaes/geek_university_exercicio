produto = float(input('Digite o valor do produto: '))

if produto <= 50:

    calc = produto + (produto * 0.05)
    print(f'Preco Antigo: {produto} -- Percentual: {5}% -- Preco Novo: {calc} -- Mensagem: Barato')

elif produto > 50 and produto <= 100:

    calc = produto + (produto * 0.1)

    if calc <= 80:
        print(f'Preco Antigo: {produto} -- Percentual: {10}% -- Preco Novo: {calc} -- Mensagem: Barato')

    elif calc > 80 and calc <= 120:
        print(f'Preco Antigo: {produto} -- Percentual: {10}% -- Preco Novo: {calc} -- Mensagem: Normal')

elif produto > 100:

    calc = produto + (produto * 0.15)

    if calc > 80 and calc <= 120:

        print(f'Preco Antigo: {produto} -- Percentual: {15}% -- Preco Novo: {calc} -- Mensagem: Normal')

    elif calc > 120 and calc <= 200:

        print(f'Preco Antigo: {produto} -- Percentual: {15}% -- Preco Novo: {calc} -- Mensagem: Caro')

    elif calc > 200:

        print(f'Preco Antigo: {produto} -- Percentual: {15}% -- Preco Novo: {calc} -- Mensagem: Muito Caro')

