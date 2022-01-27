# Um professor quer sortear um dos seus seis alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

# usar random
# o uso de str não é obrigatório

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
print(f'\nO aluno escolhido é {random.choice(lista)}')

'''from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
a6 = str(input('Sexto aluno: '))
lista = [a1, a2, a3, a4, a5, a6]
print(f'\nO aluno escolhido é {choice(lista)}')'''