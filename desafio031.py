# desenvolva um programa que pergunte a distância de uma viagem em km
# calcule o preço da passagem, cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas

dis = float(input('Qual a distância da viagem? '))
# passagem = dis * 0.5 if dis <= 200 else dis * 0.45
if dis <= 200:
    passagem = 0.5 * dis
    print(f'O valor da passagem é R${passagem:.2f}.')
else:
    passagem = 0.45 * dis
    if passagem <= 99.9:
        passagem = 100
        print(f'O valor da passagem é R${passagem:.2f}.')
    else:
        passagem = 0.45 * dis
        print(f'O valor da passagem é R${passagem:.2f}.')
