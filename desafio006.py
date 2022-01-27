# ler um número, mostrar dobro, triplo e raiz quadrada

from cmath import sqrt


num = int(input('Digite um valor para saber o dobro, triplo e raiz quadrada: '))

print(f'Dobro: {num * 2}\nTriplo: {num * 3}\nRaiz quadrada: {pow(num, (0.5)):.2f}')

# a raiz quadrada pode ser retirada pela biblioteca math com o metodo sqrt
# o numero deve ser lido com float
from math import sqrt

num = float(num)
raiz = sqrt(num)
print(raiz)
