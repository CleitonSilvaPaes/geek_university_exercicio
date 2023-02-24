for i in range(1000, 10000):
    for j in range(1000, 10000):
        str_i = str(i)
        str_j = str(j)
        
        soma = i + j
        order = soma**2
        str_order = str(order)

        if (str_i+str_j) == str_order:
            print(f'{i} + {j} = {soma}')
            print(f'{soma}² = {order}')
            