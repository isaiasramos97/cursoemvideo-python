n = int(input('Digite um número inteiro qualquer: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes, ', end='')
if tot == 2:
    print('portanto, é um número primo.')
else:
    print('portanto, não é um número primo.')
