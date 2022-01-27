# crie um programa que leia o ano de nascimento de 7 pessoas. no final, mostre quantas pessoas ainda nao
# atingiram a maioridade e quantas sao maiores. MAIORIDADE 21
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Qual o ano de nascimento da {pessoas}ª pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')
