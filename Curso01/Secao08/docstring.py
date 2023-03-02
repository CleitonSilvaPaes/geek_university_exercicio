"""
Documentando funcao com Docstrings
"""

# Exemplos
def fatorial(n:int):
    """
    Funcao recursiva dado um numero obtem o fatorial do mesmo

    Args:
        n (int): numero do elemento 

    Returns:
        _type_: retorna o fatorial do numero (n)
    """
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

# help(fatorial)
print(fatorial.__doc__)