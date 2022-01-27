# crie um programa que leia varios numeros inteiros pelo teclado. o programa só para quando o usuario digitar o valor
# 999, que é a condiçao de parada. no final, mostre quantos numeros foram digitados
# e qual foi a soma entre eles (desconsiderando o flag)
n = soma = cont = 0
mult = 1
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
    mult = mult * n
print(f'Você digitou {cont} números e a soma entre eles é {soma}.'
      f'\nA multiplicação entre todos eles é {int(mult)}')
