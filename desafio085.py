'''Crie um programa onde o usuário possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha
separados os valores pares e impares. no final, mostre os valores pares e impares em ordem crescente.'''
numbers = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    numbers.append(n)
    if n % 2 == 0 and n != 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
pares.sort()
impares.sort()
print(f'A lista completa dos números citados é {numbers}\n'
      f'Os números pares são {pares}\n'
      f'Os números ímpares são {impares}')

# outra opção

valores = [[], []]

for c in range (1, 8):
  valor = int(input(f'Digite o {c}° valor: '))
  if valor % 2 == 0 and valor != 0:
    valores[0].append(valor)
  if valor % 2 == 1:
    valores[1].append(valor)

valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados são {valores[0]}')
print(f'Os valores ímpares digitados são {valores[1]}')
