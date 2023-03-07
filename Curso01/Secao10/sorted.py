"""
Sorted

OBS: Não confunfa, apesar do nome, com a funcao sort() que na estudamos em lista. o sort() so funciona em lista.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos do iteravel ordenados

# Adicionando parametros ao sorted()
numeros = [1,2,6,5,3]
print(sorted(numeros, reverse=True))

usuarios = [
    {'username': 'samuel', 'tweets' : ['Eu adoro bolos', 'Eu adoro pizzas']},   
    {'username': 'carla', 'tweets' : ['Eu adoro gato']},   
    {'username': 'jeff', 'tweets' : []},   
    {'username': 'bob123', 'tweets' : []},   
    {'username': 'doggo', 'tweets' : ['Eu adoro cachorros', 'Vou Sair hoje']},   
    {'username': 'gal', 'tweets' : []},   
]
# Ordenando por username - Ordem Alfabetica
print(sorted(usuarios, key=lambda u: u['username']))

# Ordenando por numero de tweets
print(sorted(usuarios, key=lambda u: len(u['tweets'])))
"""

musicas = [
    {'title': 'Thunderstruck', 'tocou': 3},
    {'title': 'Dead Skin Mask', 'tocou': 2},
    {'title': 'Back in Black', 'tocou': 4},
    {'title': 'Too old to rock "in" roll, too ynoung to die', 'tocou': 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais  tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))