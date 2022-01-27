# Faça um programa que leia um numero de 0 a 9999 e mostre cada um dos dígitos separados

num = int(input('Informe um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}...\nUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')