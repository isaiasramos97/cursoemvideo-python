# faça um programa que leia um numero qualquer e mostre seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120
from math import factorial
n = int(input('Digite um número inteiro qualquer para calcular seu fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f'{factorial(n)}')
# usando for
"""for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f'{factorial(n)}')"""
