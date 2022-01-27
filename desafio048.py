# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres
# e que se encontram no intervalo de 1 até 500
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c # é a msm coisa que 's = s + c'
print(f'No intervalo entre 1 e 500, temos {cont} números ímpares múltiplos de 3, e a soma entre eles é {s}.')
