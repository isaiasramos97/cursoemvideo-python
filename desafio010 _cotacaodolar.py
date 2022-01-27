# ler quanto de dinheiro a pessoa tem e quanto ela pode comprar em dolar (5,20)

import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dolar = float(cotacoes['USDBRL']['bid'])

print(f'O dólar neste momento vale R${cotacao_dolar:.2f}')
print('Quer saber quanto você pode comprar em dólares?')
reais = float(input('Quanto você tem em reais? R$'))
compra = reais / usd
print(f'\nVocê pode comprar US${compra:.2f}.')
