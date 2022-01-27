# crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte ao usuario qual sera o valor a
# ser sacado (int) e o programa vai informar quantas cedulas de cada valor serao entregues.
# obs considere que o caixa possui cedulas de 1, 10, 20 e 50
print('-'*30+'\nBANCO VIRTUAL\n'+'-'*30)
value = int(input('Qual valor você quer sacar? '))
total = value
ballot = 50
totballot = 0
while True:
      if total >= ballot:
            total -= ballot
            totballot += 1
      else:
            print(f'Total de {totballot} cédulas de R${ballot}.')
            if ballot == 50:
                  ballot = 20
            elif ballot == 20:
                  ballot = 10
            elif ballot == 10:
                  ballot = 1
            totballot = 0
            if total == 0:
                  break
print('Volte sempre. Tenha um bom dia!')
