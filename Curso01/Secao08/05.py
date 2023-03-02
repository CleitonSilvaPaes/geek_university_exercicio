import math


def volume(r: float) -> float:
    return round((4 / 3) * math.pi * (r**3), 2)


raio = float(input('Digite o raio: '))
print(volume(raio))
