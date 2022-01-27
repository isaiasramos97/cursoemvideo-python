print('Bem vindo ao Supermercado Python!\nEstamos com promoções. Pagando em dinheiro, PIX ou cartão de débito, '
      'você tem 10% de desconto em qualquer produto.\nÀ vista no cartão de crédito, você tem 5% de desconto.\n'
      'Caso prefira pagar parcelado, em 2x você paga o preço normal, e em 3x você paga com 20% de juros.\n')
valor = float(input('\033[1;7mValor unitário do produto:\033[m R$'))
dindebito = 1
vistacred = 2
twocred = 3
threecred = 4
print('\n\033[1;7mFormas de pagamento:\033[m\n1 - Dinheiro/Débito\n2- Á vista no cartão de crédito\n'
      '3- 2x no cartão\n4- 3x ou mais no cartão')
forma = int(input('\n\033[1mForma de pagamento solicitada:\033[m '))
if forma == 1:
    print(f'\nO valor a ser pago pelo produto é de R${valor - valor * 0.1:.2f}.')
elif forma == 2:
    print(f'\nO valor a ser pago pelo produto é de R${valor - valor * 0.05:.2f}.')
elif forma == 3:
    print(f'\nO valor a ser pago pelo produto é de R${valor:.2f}, em duas vezes de R${valor / 2:.2f}.')
elif forma == 4:
    valor = valor + valor * 0.2
    vezes = int(input('\nNº de parcelas: '))
    print(f'O valor a ser pago pelo produto é de R${valor:.2f}, em {vezes}x de R${valor / vezes:.2f}, com juros.')
else:
    print('Código inválido. Tente novamente.')
