def aumentar(preco=0, porc=0, formato=False):
    """
    -> Função para aumentar o valor, com sua devida taxa de porcentagem
    :param preco: preço do produto
    :param porc: taxa de aumento
    :param formato: se o valor será mostrado com formatação monetária ou não
    :return: o valor com o seu devido aumento
    """
    res = preco + (preco * porc / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, porc=0, formato=False):
    res = preco - (preco * porc / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:.2f}".replace(".", ",")
