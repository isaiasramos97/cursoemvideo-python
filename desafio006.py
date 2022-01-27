# ler um número, mostrar dobro, triplo e raiz quadrada

num = int(input('Digite um valor para saber o dobro, triplo e raiz quadrada: '))

print(f'Dobro: {num * 2}\nTriplo: {num * 3}\nRaiz quadrada: {pow(num, (0.5)):.2f}')