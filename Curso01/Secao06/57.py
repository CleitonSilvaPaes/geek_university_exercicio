num = int(input('Digite: '))
num2 = int(input('Digite: '))
count = 0
primos = 0

if num > num2:
    num, num2 = num2, num
for i in range(num, num2+1):
   for j in range(1, num2+1):
       if i % j == 0:
           count +=1
   if count == 2:
       primos += 1
   count = 0
print(primos)