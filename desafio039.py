# faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
print('-=' * 20, '\n\033[1mALISTAMENTO MILITAR\033[m\n', '-=' * 20)
verificacao = str(input('Você já se alistou? Responda 0 para sim e 1 para não: '))
if verificacao == 0:
    print('Parabéns, você está em dia com suas obrigações. Você é um orgulho para a Nação brasileira.')
else:
    print('\nVerifique quando você deve se alistar\n')
    nascimento = int(input('Digite seu ano de nascimento: '))
    hoje = date.today()
    idade = hoje.year - nascimento
    if idade < 18:
        print(f'Você deve se apresentar à uma Junta Militar daqui a {18 - idade} anos.')
    elif idade == 18:
        print('Você deve se apresentar à uma Junta Militar neste ano. '
              'Verifique no site a Junta mais próxima de sua residência.')
    else:
        print(f'Você está em débito com sua nação. Deveria ter se apresentado há {idade - 18} ano(s).')
