# # desenv uma log que leia o peso e a alt de uma pessoa. calcule seu IMC
# e mostre seu status, de acordo com a tab abaixo
# abaixo de 18.5: abaixo do peso
# entre 18.5 a 25: peso ideal
# 25 ate 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida
# IMC = PESO / ALT²
print('-=' * 20, '\nCALCULE SEU IMC\n', '-=' * 20)
peso = float(input('Seu peso (em kg): '))
alt = float(input('Sua altura (em metros): '))
IMC = peso / alt ** 2
if IMC < 18.5:
    print(f'Seu índice de massa corporal é {IMC:.1f}. '
          f'Você está abaixo do peso. Cuide de sua saúde. Consulte um nutricionista.')
elif IMC >= 18.5 and IMC < 25:
    print(f'Parabéns, seu índice de massa corporal é {IMC:.1f}. '
          f'Você está no peso ideal para sua altura. Siga cuidando de sua saúde. Foco total.')
elif IMC >= 25 and IMC <= 30:
    print(f'Seu índice de massa corporal é {IMC:.1f}. Você está em situação de sobrepeso. '
          f'Cuide-se, consulte um nutricionista e um profissional de educação física.')
elif IMC > 30 and IMC < 40:
    print(f'Seu índice de massa corporal é {IMC:.1f}. Você está no quadro de obesidade, esta é uma situação perigosa. '
          f'Cuide-se, consulte um nutricionista e um profissional de educação física. Não deixe para se cuidar depois.')
else:
    print(f'Seu índice de massa corporal é {IMC:.1f}. Você está no quadro de obesidade mórbida, '
          f'e esta é uma situação perigosíssima. Fale com seu médico. Não deixe para se cuidar depois.')
