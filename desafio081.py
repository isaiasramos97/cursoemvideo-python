"""Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, mostre:
a) quantos numeros foram digitados
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado, está ou nao na lista"""
elements = []
while True:
    elements.append(int(input('Digite um valor: ')))
    go_on = str(input('Valor adicionado com sucesso.\nDeseja continuar? [S/N] ')).strip().upper()[0]
    while go_on not in 'SN':
        go_on = str(input('Resposta inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if go_on in 'N':
        break
print(f'Você digitou {len(elements)} valores.')
elements.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {elements}')
if 5 in elements:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
