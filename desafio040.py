# crie um programa que leia duas notas de um aluno e calcule sua media
# mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5: reprovado
# entre 5 e 6.9: recuperação
# media 7 ou sup: aprovado
print('-=' * 20, '\n\033[1mUNIVERSIDADE ESTÁCIO DE SÁ\033[m\n', '-=' * 20)
av1 = float(input('Nota da AV1: '))
av2 = float(input('Nota da AV2: '))
media = (av1 + av2) / 2
if media >= 7:
    print(f'Parabéns! Sua média neste semestre foi {media:.1f}, e você está aprovado.')
elif media < 5:
    print(f'Você foi reprovado. Sua média foi {media:.1f}. Verifique na secretaria as condições para se inscrever '
          f'nesta disciplina para o próximo semestre.')
elif 7 > media >= 5:
    print(f'Esperava mais de você. Faça a AV3 na semana que vem para poder ser aprovado. Você precisará tirar no mínimo {14 - media:.1f}.')
