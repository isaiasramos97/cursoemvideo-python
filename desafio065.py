# crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, mostre a media entre todos os
# valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuario se ele quer ou nao continuar
# a digitar valores
continua = 's'
soma = quant = media = maior = menor = 0
while continua in 'Ss':
    n = int(input('Digite um número: '))
    continua = str(input('Quer continuar [S/N]: ')).lower().strip()
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / quant
print(f'Você digitou {quant} números, a soma entre eles é {soma}, e a média de tudo é {media:.2f}')
print(f'O maior número digitado é {maior} e o menor é {menor}')
