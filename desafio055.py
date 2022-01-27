# faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'O peso da {p}ª pessoa é: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.\nO menor foi de {menor}kg.')

