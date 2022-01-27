# crie um programa que faça o computador jogar jokenpo com voce
from random import choice
from time import sleep
print('-=' * 20, '\n\033[1mVamos jogar JOKENPÔ?\033[m\n', '-=' * 20)
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
jog1 = str(input('Pedra, papel ou tesoura? '))
jog = jog1.lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if jog == 'pedra' and pc == 'papel' or jog == 'papel' and pc == 'tesoura' or jog == 'tesoura' and pc == 'pedra':
    print(f'Venci. Escolhi {pc} e você {jog}.')
elif jog == 'pedra' and pc == 'tesoura' or jog == 'tesoura' and pc == 'papel' or jog == 'papel' and pc == 'pedra':
    print(f'Você venceu. Escolhi {pc} e você {jog}.')
elif jog == pc:
    print('Empatamos. Vamos jogar novamente.')
'''for jog in jog1:
    if jog == pc:
        print('Empatamos. Vamos jogar novamente.')
        print(jog1)'''
