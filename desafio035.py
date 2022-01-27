# desenvolva um programa que leia o comprimento de três retas e
# diga ao usuario se elas podem ou não formar um triangulo
print('-=' * 20)
print('Analisando triângulos')
print('-=' * 20)

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triângulo')
else:
    print('Essas retas não formam um triângulo.')