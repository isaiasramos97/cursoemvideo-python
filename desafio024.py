# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
city = str(input('Digite um nome de sua cidade: ')).strip()
print(city[:5].upper() == 'SANTO')

