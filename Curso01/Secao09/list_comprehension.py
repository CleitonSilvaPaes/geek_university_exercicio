"""
List Comprehension

- Utilizando List Comprehension podemos gerar novas listas com daos processados a partir de outro interavel.

# Sintaxe da List Comprehension

[ dado for dado in interavel ]

# Exemplos

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]

Para entrender melhor o que esta acontencendo devemos dividir a expressao em duas partes: 
 - A primeira parte: for numero in numeros
 - A segunda parte: numero * 10
 
def funcao(valor):
    return valor**2
    
res = [funcao(i) for i in numeros]
>>> [1, 4, 9, 16, 25]

List Comprehension com IF

[f(x) if condition else g(x) for x in sequence] - Nesse exemplo ira acontecer uma coisa ou outra
[f(x) for x in sequence if condition] - Nesse de modo para filtrar elementos

Exemplo
[x for x in range(1, 10) if x % 2 and  x % 3 == 0]
new_list = []
for x in range(1, 10):
    if x % 2 == 0 and x % 3 == 0:
        new_list.append(x)

Lista Aninhadas
- Algumas liguagens de programacao possuem uma estrura de dadps chamadas de arrays:
    - Unidimensionais (Arraus/ Vetores);
    - Multidimensionais (Matrizes);
    
Em Python nos temos as Listas



"""