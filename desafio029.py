# Escreva um programa que leia a velocidade de um carro

# se ele ultrapassar 80kmh mostre uma mensagem dizendo que ele foi multado
# a multa vai custar 97,57 + 7,23 por cada km acima do limite
from time import sleep

vel = float(input('Em que velocidade o carro passou pelo radar? '))
print('Verificando...')
sleep(1)
if vel > 80.0:
    multa = 97.57 + 7.23 * (vel - 80)
    print(f'O motorista será multado e deverá pagar o valor de R${multa:.2f}.')
else:
    print('O carro passou dentro da velocidade permitida.')
