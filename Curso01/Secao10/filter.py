"""
Filter

filter() -> Serve para filtrar dados de uma determinada colecao.

-----------------------------------------------------------------------------------------------------------

# biblioteca para trabalhar com dados estaticos
import statistics

# Dados coletados de algum sensor
valores = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calcular a media dos dados utilizando a funcao mean()
media = statistics.mean(valores)

# OBS: Assim como a funcao map(), a filter() recebe dois parametros
# sendo uma funcao e um interavel.

# OBS: Assim como na funcao map(), apos serem utilizados os dados de filter eles são excluidos da memoria

res = filter(lambda x: x > media, valores)
print(list(res))


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(list(filter(None, paises)))
>>> ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

# A diferenca entre map() e filter() é:

# map() -> Recebe dois paramentros, uma funcao e um iteravel e retorna um objeto mapeando a funcao para cada elemento do interavel

# filter() -> Recebe dois parametros, uma funcao e um interavel e retorna um objeto filtrando apenas os elementos de acordo com filtro.


# Exemplo mais complexo
usuarios = [
    {'username': 'samuel', 'tweets' : ['Eu adoro bolos', 'Eu adoro pizzas']},   
    {'username': 'carla', 'tweets' : ['Eu adoro gato']},   
    {'username': 'jeff', 'tweets' : []},   
    {'username': 'bob123', 'tweets' : []},   
    {'username': 'doggo', 'tweets' : ['Eu adoro cachorros', 'Vou Sair hoje']},   
    {'username': 'gal', 'tweets' : []},   
]

# Filtar os usuarios que estao inativos no Twitter
# # Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# # Forma 2
# inativos = list(filter(lambda u: not len(u['tweets']), usuarios))
# print(inativos)

"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutrura é' + nome, desde que cada nome tenha monos de 5 caracteres

print(list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))))