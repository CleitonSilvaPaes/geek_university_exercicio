premio = 780_000_000

ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio - (ganhador1 + ganhador2)
# # ganhador3 = premio * 0.22

print(f'''\nPrimeiro Ganhador: {ganhador1}\n
Segundo Ganhador: {ganhador2}\n
Terceiro Ganhador: {ganhador3}\n''')