# crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
# depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
import re

palavras = ('APRENDER', 'ESTUDAR', 'TRABALHAR', 'PYTHON', 'PARAISO',
            'CARTA', 'ENTREGA', 'VENDER', 'MERGULHO', 'OSSO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')

vogais = re.compile(r'[aeiouAEIOU]')  # utilizacao de regex. aprendido no livro "automatize tarefas maçantes com python"
lista_das_vogais = vogais.findall(str(palavras))
print()
print('-='*30)
print(f'{len(lista_das_vogais)} vogais')
