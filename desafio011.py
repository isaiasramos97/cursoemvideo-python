# ler a largura e a altura da parede, calcular a área, e a quantidade de tinta necessária para pintar toda a parede
# 1L equivale a 2m²

print('Saiba o quanto de tinta você precisa para pintar uma parede!')
l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
tinta = a / 2

print(f'A área da parede é {a:.2f}m², sendo assim, você precisa de {tinta:.3f} litros de tinta para pintar toda a parede.')