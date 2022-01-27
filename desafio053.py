# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
# ex: frases iguais de tras pra frente
# apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona
frase = str(input('Digite uma palavra ou frase para verificarmos se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertida = str(junto[::-1])
'''invertida = ''
for letra in range(len(junto) -1, -1, -1):
    invertida += junto[letra]'''
print(f'O inverso de {junto} é {invertida}.')
if junto == invertida:
    print('Sendo assim, este termo que você digitou é um palíndromo.')
else:
    print('Sendo assim, este termo não é um palíndromo.')
