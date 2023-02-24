print("""
------------------------------------
| Especificacao   | Codigo | Preco |
| Cachorro Quente |  100   | 1.20  |
| Bauru Simples   |  101   | 1.30  |
| Bauru com Ovo   |  102   | 1.50  |
| Hamburguer      |  103   | 1.20  |
| Cheeseburguer   |  104   | 1.70  |
| Suco            |  105   | 2.20  |
| Refrigerante    |  106   | 1.00  |
------------------------------------
""")

cod = int(input('Digite o codigo do cardapio: '))
qtd = int(input('Digite a quantidade: '))

if cod == 100:
    print(f'Cachorro Quente --- {qtd * 1.20}')
elif cod == 101:
    print(f'Bauru Simples --- {qtd * 1.30}')
elif cod == 102:
    print(f'Bauru com Ovo --- {qtd * 1.50}')
elif cod == 103:
    print(f'Hamburguer --- {qtd * 1.20}')
elif cod == 104:
    print(f'Cheeseburguer --- {qtd * 1.70}')
elif cod == 105:
    print(f'Suco --- {qtd * 2.20}')
elif cod == 106:
    print(f'Refrigerante --- {qtd * 1.00}')
else:
    print('Codigo invalido')