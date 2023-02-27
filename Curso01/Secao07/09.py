pares = []
count = 1

rodar = True

while rodar:
    if count == 6:
        rodar = False
    x = int(input('Digite um numero par: '))
    
    if x % 2 == 0:
        pares.append(x)
        count+=1

print('Numeros pares lidos na ordem inversa: ', *pares[::-1])
