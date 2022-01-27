# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''sexo = 0
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: [F/M] ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('\033[0;31mO termo digitado é inválido. Digite "F" para feminino e "M" para masculino.\033[m')
print('Obrigado pela informação.')'''

sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper() [0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [F/M] ')).strip().upper() [0]
if sexo in 'F':
    print('Sexo feminino registrado com sucesso.')
elif sexo in 'M':
    print('Sexo masculino registrado com sucesso.')
