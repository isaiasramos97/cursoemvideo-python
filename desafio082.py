numbers = list()
even_numbers = list()
odd_numbers = list()

while True:
    numbers.append(int(input('Digite um valor: ')))
    go_on = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while go_on not in 'SN':
        go_on = str(input('Resposta inválida. Deseja continuar? ')).strip().upper()[0]
    if go_on in 'N':
        break
for v in numbers:
    if v % 2 == 0 and v != 0:
        even_numbers.append(v)
    elif v % 2 == 1:
        odd_numbers.append(v)

print(f'Lista gerada com todos os valores digitados: {numbers}')
print(f'Valores pares: {even_numbers}')
print(f'Valores ímpares: {odd_numbers}')

if 0 in numbers:
    print('O valor 0 está na lista.')
else:
    print('O valor 0 não está na lista')
