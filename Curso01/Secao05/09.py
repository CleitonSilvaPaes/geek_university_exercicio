salario = float(input('Digite salario: '))
prestacao = float(input('Digite valor da prestacao: '))

calc_porcentacem = (prestacao*100)/salario

if calc_porcentacem <= 20:
    print('Emprestimo concedido')
else:
    print('Emprestimo nao concedido')