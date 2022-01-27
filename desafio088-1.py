from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30 + '\nPALPITES DA LOTOFACIL\n' + '-' * 30)
qtd = int(input('Quantos jogos você quer gerar? '))
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        numero = randint(1, 25)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 15:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"SORTEANDO {qtd} JOGOS..."), sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(l)}')
    sleep(1)
print('BOA SORTE!')