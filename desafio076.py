# crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia
# no final, mostre uma listagem de preços, organizando os dados em forma tabular
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.90,
         'Canetas', 22.35,
         'Livro', 34.90)
print('-'*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)
