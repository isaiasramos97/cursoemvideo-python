# refaça o desafio 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while
print('-=' * 20, '\nGERADOR DE PA\n' + '-=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')