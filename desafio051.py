# desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final, mostre os 10 primeiros termos dessa
# progressão
print('=' * 20, '\n10 TERMOS DE UMA PA\n' + '=' * 20)
pa = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = pa + (10-1) * r
for c in range(pa, decimo + r, r):
    print(f'{c} ', end='-> ')
print('acabou')
