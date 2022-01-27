# escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento
# para salarios superiores a 1250, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%
atual = float(input('Digite seu salário: R$'))
if atual > 1250:
    novo = atual + atual * 0.1
    print(novo)
elif atual + atual * 0.1 < 1437.5:  # elif aprendido na aula 12, após a execução deste exercício
    novo = 1437.5
    print(novo)
else:
    novo = atual + atual * 0.15
    print(novo)
