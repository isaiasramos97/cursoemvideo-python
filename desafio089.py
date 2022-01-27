"""crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
no final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno
individualmente."""
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    go_on = str(input('Deseja continuar? ')).strip().upper()[0]
    if go_on not in 'SN':
        go_on = str(input('Resposta inválida. Deseja continuar? ')).strip().upper()[0]
    if go_on in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
