soma = 0

numeros = {
    1:2,
    2:4,
    3:4,
    4:6,
    5:5,
    6:4,
    7:4,
    8:4,
    9:4,
    10:3,
    11:4,
    12:4,
    13:5,
    14:8,
    15:6,
    16:9,
    17:9,
    18:7,
    19:8,
    20:5,
    30:6,
    40:8,
    50:9,
    60:7,
    70:7,
    80:7,
    90:7,
    100:3,
    200:8,
    300:9,
    400:12,
    500:13,
    600:13,
    700:10,
    800:10,
    900:10,
    1000:3
}

for i in range(1, 7):
    if i >= 1 and i <=20:
       soma += numeros[i]
    else:
        num1 = len(str(i))
        if num1 == 2:
            num1 = str(i)[0]
            num2 = str(i)[1]
            num1 = int(num1)*10
            num2 = int(num2)
            soma+= numeros[num1]
            if num2 != 0:
                soma+= numeros[num2]
        elif num1 == 3:
            num1 = str(i)[0]
            num2 = str(i)[1]
            num3 = str(i)[2]
            num1 = int(num1)*100
            num2 = int(num2)*10
            num3 = int(num3)
            soma+= numeros[num1]
            if num2 != 0:
                soma+= numeros[num2]
            if num3 != 0:
                soma+= numeros[num3]
        else:
            soma+= numeros[1000]
print(soma)