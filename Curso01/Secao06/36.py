soma_dos_quadadros = 0
soma_dos_numeros = 0
for i in range(1, 10+1):
    soma_dos_quadadros += i**2
    soma_dos_numeros += i

soma_dos_numeros **= 2

print(f'Soma dos Quadrados: {soma_dos_quadadros}')
print(f'Soma dos Numeros Quadrados: {soma_dos_numeros}')
print(f'Diferenca: {soma_dos_numeros - soma_dos_quadadros}')
