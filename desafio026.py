# Crie um programa que leia uma frase e diga quantas vezes aparece a letra a
# em que posição ela aparece na primeira vez
# em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()    # strip tira espaços indesejados
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
