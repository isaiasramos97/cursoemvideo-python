# crie um programa que leia o nome e o preço de varios produtos. o programa deverá perguntar se o usuário vai continuar.
# no final, mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de 1000 reais
# qual é o nome do produto mais barato.
print('{:-^40}'.format('MERCADÃO ELETRONICS'))
total = thousand = cheaper = items = 0
name_cheaper = ' '
while True:
    product = str(input('Produto: ')).strip()
    price = float(input('Preço: R$'))
    items += 1
    total += price
    if price > 1000:
        thousand += 1
    if items == 1 or price < cheaper:
        cheaper = price
        name_cheaper = product
    go_on = ' '
    while go_on not in 'SN':
        go_on = str(input('Deseja adicionar mais algum produto? [S/N] ')).strip().upper()[0]
    if go_on == 'N':
        break
print(f'Nesta compra foram registrados {items} produtos. O total gasto foi de R${total:.2f}.\n'
      f'{thousand} produtos custaram mais de R$1000.\nO produto mais barato foi {name_cheaper}, que custou {cheaper:.2f}.')
