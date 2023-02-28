from random import randrange
n = 10
vet = [randrange(1,100) for i in range(n)]
media = sum(vet)/len(vet)
soma = 0

print(vet)
for i in vet:
    soma += (i - media)**2

dp = (soma / (n-1))**(1/2)

print(f'Desvio Padrao: {dp}')