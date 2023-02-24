IMPOSTO = 0.07
GRATIFICACAO = 0.05
salario_base = float(input('Digite o salario base: '))

calc = salario_base - (salario_base * IMPOSTO) + (salario_base * GRATIFICACAO)

print(calc)