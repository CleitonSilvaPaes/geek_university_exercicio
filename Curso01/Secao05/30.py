num1 = float(input('Digite o numero 1°: '))
num2 = float(input('Digite o numero 2°: '))
num3 = float(input('Digite o numero 3°: '))

if num1 >= num2 >= num3:
    print(num3, num2, num1)
elif num1 >= num3 >= num2:
    print(num2, num3, num1)
elif num2 >= num1 >= num3:
    print(num3, num1, num2)
elif num2 >= num3 >= num1:
    print(num1, num3, num2)
elif num3 >= num1 >= num2:
    print(num2 ,num1 ,num3)
elif num3 >= num2 >= num1:
    print(num1, num2, num3)