rodando = True
maior = 0
menor = 0
count = 0
while rodando:
    n = int(input('Digite: '))
    if n == 0:
        rodando = False
    elif count == 0:
        maior, menor = n, n
    elif maior < n:
        maior = n
    elif menor > n:
        menor = n
        
    count+=1
print(maior, menor)