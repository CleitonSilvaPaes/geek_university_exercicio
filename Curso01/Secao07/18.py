from math import gcd
vetor = [1,2,3,4,5,6,7,8,9,10,11,12,21]

x = int(input('Digite um numero: '))

for i in vetor:
    if x % i == 0:
        print(i, end=' ')