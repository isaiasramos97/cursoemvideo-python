# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
# depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Eu sorteei os valores {numeros}')
print(f'O maior número é {max(numeros)}\nO menor número é {min(numeros)}')