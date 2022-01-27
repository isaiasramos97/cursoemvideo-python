# melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais termos. o programa encerra quando ele
# disser que quer mostrar 0 termos.
print('-=' * 20, '\nGERADOR DE PA\n' + '-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver? '))
print(f'Progressão finalizada. Foram mostrados {total} termos.')
