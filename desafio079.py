# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. caso o numero ja
# exista la dentro, ele nao sera adicionado. no final, serão exibidos todos os valores unicos digitados,
# em ordem crescente.
numbers = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não será adicionado à lista.')
    go_on = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while go_on not in 'SN':
        go_on = str(input('Resposta inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if go_on in 'N':
        break
numbers.sort()
print(f'Você digitou os valores {numbers}')
