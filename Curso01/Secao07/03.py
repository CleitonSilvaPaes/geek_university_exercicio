lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
for i in lista:
    lista2.append(i**2)

print('Lista original: ',*lista)
print('Lista com os valores ao quadrado: ',*lista2)