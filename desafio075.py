# desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
# no final mostre:
# quantas vezes apareceu o valor 4
# em que posição foi digitado o primeiro valor 3
# quais foram os números pares
valores = (int(input('Insira um número: ')),
           int(input('Insira outro número: ')),
           int(input('Insira mais um número: ')),
           int(input('Insira o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
