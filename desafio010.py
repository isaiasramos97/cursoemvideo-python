# ler quanto de dinheiro a pessoa tem e quanto ela pode comprar em dolar (5,20)

print('Quer saber quanto você pode comprar em dólares?')
reais = float(input('Quanto você tem em reais? R$'))
usd = 5.20
compra = reais / usd

print(f'\nVocê pode comprar US${compra:.2f}.')