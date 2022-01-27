v = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    v += n
    soma += n
print(f'A soma entre os {v} valores que você digitou é {soma}.')