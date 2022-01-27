# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras o nome tem
# Quantas letras tem o primeiro nome
completo = str(input('Digite seu nome completo: ')).strip()
separa = completo.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {completo.upper()}')
print(f'Seu nome em minúsculas é {completo.lower()}')
print(f'Seu nome ao todo tem {len(completo) - completo.count(" ")} letras.')
# print(f'Seu primeiro nome tem {completo.find(" ")} letras.')
print(f'Seu primeiro nome tem {len(separa[0])} letras.')