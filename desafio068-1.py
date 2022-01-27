from random import randint
win = 0
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR?')
while True:
    player = int(input('Diga um valor [0~10]: '))
    computer = randint(0,10)
    total = player+computer
    odd_or_even = ' '
    while odd_or_even not in 'PI':
        odd_or_even = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {computer}. Total de {total}.', end=' ')
    print('Deu par.' if total % 2 == 0 else 'Deu ímpar.')
    if odd_or_even == 'P':
        if total % 2 == 0:
            print('Você venceu')
            win += 1
        else:
            print('Você perdeu.')
            break
    elif odd_or_even == 'I':
        if total % 2 == 1:
            print('Você venceu.')
            win += 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {win} vezes.')
