# Melhore o jogo do desafio 28, onde o computador vai pensar em um número entre 0 e 10. Só que agora,
# o jogador vai tentar adivinhar até acertar. Mostrando quantos palpites foram necessários para vencer
from random import randint
computador = randint(1, 10)
print('Sou o seu computador. Acabei de pensar em um número entre 1 e 10.\nSerá que você consegue adivinhar qual foi?.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tenta mais uma vez.')
        elif jogador > computador:
            print('Menos... tenta mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
