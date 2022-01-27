# ler o salario de um funcionario, e mostrar seu novo salario com um aumento de 15%

salario = float(input('O salário do funcionário é '))
aumento = salario * 0.15
novo = salario + aumento
print(f'E o novo salário dele, com o aumento que estamos dando, ficará em {novo:.2f}')