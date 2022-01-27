from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR?')
cont = 0
while True:
    comp = randint(0, 10)
    print('-='*30)
    valor = int(input('Diga um valor: [0~10] '))
    PI = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    if PI == 'P':
        PI = 'par'
    elif PI == 'I':
        PI = 'ímpar'
    total = comp+valor
    if total % 2 == 0:
        result = 'par'
        if PI == result:
            winlose = 'venceu'
            print(f'Você jogou {valor} e o computador {comp}. Total {total}, deu {result}, você {winlose}. '
                  f'Vamos jogar mais uma.')
        else:
            winlose = 'perdeu'
            break
    else:
        result = 'ímpar'
        if PI == result:
            winlose = 'venceu'
            print(f'Você jogou {valor} e o computador {comp}. Total {total}, deu {result}, você {winlose}. '
                  f'Vamos jogar mais uma.')
        else:
            winlose = 'perdeu'
            break
    cont += 1
print(f'Você jogou {valor} e o computador {comp}. Total {total}, deu {result}, você {winlose}. Você ganhou {cont} vezes'
      f' consecutivas.')
