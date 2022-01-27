# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
# O código de cima foi a resolução do Guanabara. Não funcionou por alguma incompatibilidade.

import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print(input('Está ouvindo?'))