"""Crie um programa onde o usuario possa digitar 5 valores numericos e cadastre-os
em uma lista, ja na posicao correta, sem usar o sort().
no final, mostre a lista ordenada na tela"""
lista = []
for c in range(0,5):
    n = int(input('Insira um número na lista: '))
    if c == 0 or n > lista[len(lista)-1]:  # lista[-1] daria no mesmo
        lista.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')