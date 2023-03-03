def to_farenheit(celsius: float) -> float:
    return celsius * (9/5) + 32

x = float(input('Digite uma temperatura em celsius: '))
print(to_farenheit(x))