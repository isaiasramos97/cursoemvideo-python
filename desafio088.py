"""faça um programa que ajude o jogador da mega sena a criar palpites.
o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60
para cada jogo. cadastrando tudo em uma lista composta"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30 + '\nPALPITES DA MEGA SENA\n' + '-' * 30)
qtd = int(input('Quantos jogos você quer gerar? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"SORTEANDO {qtd} JOGOS..."), sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(l)}')
    sleep(1)
print('BOA SORTE!')
"""# from time import sleep

qtd = int(input('Quantos jogos você quer que eu sugira? '))
jogo = list()

for jogos in range(0, 6):
    jogo.append(randint(1, 60))
print(jogo)
# print(f'Minha sugestão é: {jogos}')"""
