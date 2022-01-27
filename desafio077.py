# crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
# depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
import string
palavras = ('APRENDER','ESTUDAR', 'TRABALHAR', 'PYTHON', 'PARAISO',
            'CARTA', 'ENTREGA', 'VENDER', 'MERGULHO', 'OSSO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
