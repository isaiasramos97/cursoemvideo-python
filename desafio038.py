# escreva um programa que leia dois numeros inteiros e compare-os.
# mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais
n1 = int(input('Dê um número inteiro: '))
n2 = int(input('Dê mais um: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
