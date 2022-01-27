# desenvolva um programa que leia nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
somaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade:.1f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
