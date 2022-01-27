# Crie uma tupla preenchida com os 20 primeiros colocados do brasileirão. na ordem de colocação. depois mostre:
# apenas os 5 primeiros colocados
# os ultimos 4 colocados
# uma lista com os times em ordem alfabetica
# em que posição está o time da chapecoense
times = ('Galo', 'Palmeiras', 'Fortaleza', 'RB Bragantino', 'Flamengo', 'CAP', 'Atletico-GO', 'Ceará',
         'Internacional', 'Santos', 'Corinthians', 'Juventude', 'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá', 'Sport',
         'América-MG', 'Grêmio', 'Chapecoense')
print(f'Os cinco primeiros colocado são {times[0:5]}')
print(f'Os quatro últimos são {times[-4:]}')
print(f'A lista dos times em ordem alfabética é: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
