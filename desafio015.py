# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60/dia e R$0,15 por km rodado

d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos nesses dias? '))
pagar = d * 60 + km * 0.15
print(f'\nO valor a ser pago à locadora é de R${pagar:.2f}')
