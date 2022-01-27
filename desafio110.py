"""
Adicione ao modulo moeda.py uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções
que ja temos no modulo criado até aqui.
"""
from ex110 import moeda

p = float(input("Digite o preço: R$"))
moeda.resumo(p, 10, 5)