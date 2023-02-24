jogador1 = float(input('Valor investido: '))
jogador2 = float(input('Valor investido: '))
jogador3 = float(input('Valor investido: '))

valor_do_premio = float(input('Valor do premio: '))

total_inventido = jogador1 + jogador2 + jogador3

premio1 = (valor_do_premio * (jogador1/total_inventido))
premio2 = (valor_do_premio * (jogador2/total_inventido))
premio3 =  (valor_do_premio * (jogador3/total_inventido))

print(f'Amigo 1 ira ganhar: {premio1:.2f}')
print(f'Amigo 2 ira ganhar: {premio2:.2f}')
print(f'Amigo 3 ira ganhar: {premio3:.2f}')