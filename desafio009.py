tab = int(input('Digite aqui o valor que você quer saber a tabuada: '))
print(f'{tab} x {1:2} = {tab*1}')
print(f'{tab} x {2:2} = {tab*2}')
print(f'{tab} x {3:2} = {tab*3}')
print(f'{tab} x {4:2} = {tab*4}')
print(f'{tab} x {5:2} = {tab*5}')
print(f'{tab} x {6:2} = {tab*6}')
print(f'{tab} x {7:2} = {tab*7}')
print(f'{tab} x {8:2} = {tab*8}')
print(f'{tab} x {9:2} = {tab*9}')
print(f'{tab} x {10:2} = {tab*10}')

# utilizando conhecimentos mais avançados:
def tabuada(num):
    for n in range (1, 11,):
        print(f'{num} x {n} = {num * n}')


numero = int(input('Digite aqui o valor que você quer saber a tabuada: '))
tabuada(numero)
