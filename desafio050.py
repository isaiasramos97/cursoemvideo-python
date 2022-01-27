# desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for impar, desconsidere-o
s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Dê um número inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você informou {cont} números pares, e a soma entre eles é {s}.')
