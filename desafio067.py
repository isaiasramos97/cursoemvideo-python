# Faça um programa que mostre a tabuada de varios numeros
# um de cada vez, para cada valor digitado pelo usuario.
# o programa sera interrompido quando o numero solicitado for negativo
from time import sleep
print('Este programa mostra a tabuada de qualquer valor inteiro positivo que você quiser.'
      '\nPara pará-lo, digite um valor negativo')
sleep(1)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
