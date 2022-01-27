# faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
print('Digite 3 valores abaixo')
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
v3 = int(input('Valor 3: '))
# Verificando quem é menor
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
# verificando o maior
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O menor valor digitado foi \033[0;31m{menor}\033[m.\nO maior valor digitado foi \033[0;32m{maior}\033[m.')
