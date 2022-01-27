# a conf nac de nataçao precisa de um programa que leia o ano de nasci de um atleta e mostre sua categoria,
# de acordo com a idade; até 9 anos: mirim; até 14: infantil; até 19: junior; até 21: senior; acima: master;
from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Júnior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
