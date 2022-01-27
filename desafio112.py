"""
dentro do pacote utilidadesCeV que criamos no desafio 111, temos um modulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""
from ex111.utilidadescev import moeda, dado

p = dado.leiadinheiro("Digite o valor: ")
moeda.resumo(p, 10, 5)
