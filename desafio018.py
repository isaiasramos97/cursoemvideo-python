# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# python.org library reference
'''from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você deseja: '))

print(f'Seno: {sin(radians(ang)):.2f}')
print(f'Cosseno: {cos(radians(ang)):.2f}')
print(f'Tangente: {tan(radians(ang)):.2f}')'''

'''import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f'Seno de {ângulo} é {seno:.2f}, cosseno é {cosseno:.2f} e tangente é {tangente:.2f}')

from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))

print(f'Seno de {an} é {seno:.2f}, cosseno é {cosseno:.2f} e tangente é {tangente:.2f}')'''

from math import radians, sin, cos, tan
an = float(input('Ângulo: '))
print(f'Seno: {sin(radians(an)):.2f}\nCosseno: {cos(radians(an)):.2f}\nTangente: {tan(radians(an)):.2f}')