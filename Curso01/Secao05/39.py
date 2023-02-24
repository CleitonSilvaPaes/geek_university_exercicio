salario = float(input('Digite seu salario: '))
tempo = float(input('Digite seu tempo de sevico: '))

BONUS = {
    0: 'Sem bonus',
    1: 100,
    4: 200,
    7: 300,
    10: 500
}

if salario <= 500.00:
    novo_salario = salario + (salario * 0.25)
    if tempo <= 1:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[0]}
        """)
    elif tempo > 1 and tempo <= 3:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[1]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[1]}
        """)
    elif tempo >= 4 and tempo <= 6:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[4]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[4]}
        """)
    elif tempo >= 7 and tempo <= 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[7]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[7]}
        """)
    elif tempo > 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[10]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[10]}
        """)

elif salario > 500 and salario <= 1000:
    novo_salario = salario + (salario * 0.20)
    if tempo <= 1:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[0]}
        """)
    elif tempo > 1 and tempo <= 3:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[1]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[1]}
        """)
    elif tempo >= 4 and tempo <= 6:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[4]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[4]}
        """)
    elif tempo >= 7 and tempo <= 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[7]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[7]}
        """)
    elif tempo > 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[10]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[10]}
        """)

elif salario > 1000 and salario <= 1500:
    novo_salario = salario + (salario * 0.15)
    if tempo <= 1:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[0]}
        """)
    elif tempo > 1 and tempo <= 3:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[1]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[1]}
        """)
    elif tempo >= 4 and tempo <= 6:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[4]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[4]}
        """)
    elif tempo >= 7 and tempo <= 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[7]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[7]}
        """)
    elif tempo > 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[10]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[10]}
        """)

elif salario > 1500 and salario <= 2000:
    novo_salario = salario + (salario * 0.10)
    if tempo <= 1:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[0]}
        """)
    elif tempo > 1 and tempo <= 3:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[1]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[1]}
        """)
    elif tempo >= 4 and tempo <= 6:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[4]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[4]}
        """)
    elif tempo >= 7 and tempo <= 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[7]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[7]}
        """)
    elif tempo > 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[10]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[10]}
        """)

else:
    novo_salario = salario
    if tempo <= 1:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[0]}
        """)
    elif tempo > 1 and tempo <= 3:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[1]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[1]}
        """)
    elif tempo >= 4 and tempo <= 6:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[4]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[4]}
        """)
    elif tempo >= 7 and tempo <= 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[7]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[7]}
        """)
    elif tempo > 10:
        print(f"""
        Salario Atual: {salario}
        Reajuste: {novo_salario+BONUS[10]}
        Tempo de Servico: {tempo}
        Bonus: {BONUS[10]}
        """)