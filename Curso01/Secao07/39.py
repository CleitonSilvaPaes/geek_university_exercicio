numeros = int(input('Digite um valor: '))

"""
Formula

   n!
-------
k!(n-k)!
"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n *  fatorial(n-1)

for i in range(numeros):
    pascal = []
    for j in range(i+1):
        calc = int(fatorial(i)/(fatorial(j)*(fatorial(i-j))))
        pascal.append(calc)
    print(*pascal)