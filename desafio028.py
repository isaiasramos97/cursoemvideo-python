# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

#O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep
num = randint(0, 5) # randomiza numeros inteiros
print('Descubra o número sorteado pelo computador.\nSerá sorteado um número inteiro de 0 a 5.\nSe você acertar, ganha 10 reais.')
escolhido = str(input('Qual número você acha que será sorteado? '))
print('Sorteando...')
sleep(2)    # wait por 2 segundos
print(f'O número sorteado é {num}.')
if num == escolhido:
    print('Parabéns!! Você acertou!!')
else:
    print('Que pena. Você errou.')
