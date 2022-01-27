# faça um algoritmo que leia o preço do produto e mostre o novo preço com 5% de desconto

produto = float(input('O valor da camisa é '))
desconto = produto * 0.05
descontado = produto - desconto
print(f'Todos os nossos sócios têm 5% de desconto, então poderão pagar {descontado:.2f} pela camisa.')
