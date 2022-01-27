# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa

# a² = b² + c²

from math import sqrt
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('E a medida do cateto adjascente? '))
hip = sqrt(co ** 2 + ca ** 2)

print(f'O comprimento da hipotenusa é {hip:.2f}!')

from math import hypot

co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('E a medida do cateto adjascente? '))
hipo = hypot(co, ca)

print(f'O comprimento da hipotenusa é {hipo:.2f}!')