"""Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
no final, mostre:
a) quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves"""
nome_peso_temp = list()
nome_peso_princ = list()

while True:
    nome_peso_temp.append(str(input('Nome: ')))
    nome_peso_temp.append(float(input('Peso: ')))
    if len(nome_peso_princ) == 0:
        mai = men = nome_peso_temp[1]
    else:
        if nome_peso_temp[1] > mai:
            mai = nome_peso_temp[1]
        if nome_peso_temp[1] < men:
            men = nome_peso_temp[1]
    nome_peso_princ.append(nome_peso_temp[:])
    nome_peso_temp.clear()

    go_on = str(input('Deseja continuar? ')).strip().upper()[0]
    if go_on not in 'SN':
        go_on = str(input('Resposta inválida. Deseja continuar? ')).strip().upper()[0]
    elif go_on in 'N':
        break

print(f'Você cadastrou {len(nome_peso_princ)} pessoas no banco de dados.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in nome_peso_princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
for p in nome_peso_princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
