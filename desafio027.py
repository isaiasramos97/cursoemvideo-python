# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente
# ex: ana maria braga
# primeiro: ana
# último: braga

comp = str(input('Digite seu nome completo: ')).strip()
nome = comp.title().split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')