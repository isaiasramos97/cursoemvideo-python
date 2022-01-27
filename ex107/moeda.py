def aumentar(preco, porc):
    res = preco + (preco * porc / 100)
    return res


def diminuir(preco, porc):
    res = preco - (preco * porc / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res
