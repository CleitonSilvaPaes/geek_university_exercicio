n = int(input('Digite um numero: '))
harmonico = 1

for i in range(2, n+1):
    harmonico += (1/i)
print(harmonico)