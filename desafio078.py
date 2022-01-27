# Faça um programa que leia 5 valores numericos e guarde-os em uma lista
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes nas lista
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
