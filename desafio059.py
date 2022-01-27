# crie um programa que leia dois valores e mostre um menu na tela
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('\nQual a operação desejada?\n\n[1] Somar\n[2] Multiplicar\n[3] Maior\n'
                  '[4] Digitar novos números\n[5] Sair\n')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif opcao == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2}, o maior é {n2}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
print('Fim do programa! Volte sempre!')
