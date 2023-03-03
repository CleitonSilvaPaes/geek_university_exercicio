pi = 3.141592

def volume(raio:float = 0, altura:float = 0) -> float:
    return pi * (raio**2) * altura

raio = float(input('Digite o raio: '))
altura = float(input('Digite o altura: '))

print(volume(altura=altura, raio=raio))