# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa;
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado;

casa = float(input('Valor da casa: '))
salario = float(input('Salário do requerente: '))
tempo = int(input('Prestações: '))
pmes = casa / tempo
minimo = salario * 0.3
if pmes > minimo:
    print(f'O empréstimo não foi liberado, '
          f'pois o valor das prestações (R${pmes:.2f}) é maior que 30% do salário do requerente.')
elif pmes <= minimo:
    print(f'Empréstimo liberado. O valor das prestações a serem pagas em {tempo} meses é de R${pmes:.2f}.')
