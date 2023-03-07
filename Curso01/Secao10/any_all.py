"""
Any e All

all() -> Retorna True se todos os elemtentos do interal sao verdadeiros ou ainda se o iteravel esta vazio

# Exemplo all()
nomes = ['Carlos', 'Camila', 'Carla']
print(all([nome[0] == 'C' for nome in nomes]))
>>> True

# OBS: Um iteravel vazio convertido em boolean e false, mas o all() entende com True

print(all([letra for letra in 'eio' if letra in 'aeiou']))
>>> True

[letra for letra in 'eio' if letra in 'aeiou'] # Funciona como o filter
>>> ['e', 'i', 'o']

 Equivalente a:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

--------------------------------------------------------------------------------

Any -> Retorna True se algum elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorne False. Equivalente a:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
    
print(any([0, 1, 2, 3, 4]))
>>> True
print(any([0, False, {}, (), []]))
>>> False
"""