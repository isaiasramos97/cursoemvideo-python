adults = men = women = women20 = old = count = 0
while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo? [F/M] ')).strip().upper()[0]
    if age >= 18:
        adults += 1
    if age >= 65:
        old += 1
    if sex == 'M':
        men += 1
    if sex == 'F':
        women += 1
    if sex == 'F' and age < 20:
        women20 += 1
    go_on = ' '
    while go_on not in 'SN':
        go_on = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    count += 1
    if go_on == 'N':
        break
print(f'Foram registradas {count} pessoas. Sendo elas:\n'
      f'{old} idosas.\n'
      f'{adults} maiores de 18 anos.\n'
      f'{men} homens.\n'
      f'{women} mulheres, sendo {women20} com menos de 20 anos.')
