def verifica_numero(n:int):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    return -1

print(verifica_numero(5))
print(verifica_numero(0))
print(verifica_numero(-4))