"""Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressao passada está com os parênteses abertos e fechados na ordem correta"""
xpression = str(input('Digite uma expressão: ')).strip()
pilha = []
for symbol in xpression:
    if symbol == '(':
        pilha.append('(')
    elif symbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
