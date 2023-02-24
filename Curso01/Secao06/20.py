x = int(input('Digite um numero: '))
count  = 0
par = 0
while x != 1000:
    if x % 2 == 0:
        par+=1
    count += 1
    x = int(input('Digite um numero: '))

print(f'numeros lido par: {par} -- todas as execucao {count}')