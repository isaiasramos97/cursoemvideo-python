def contador(i, f, p):
    """
    => Faz uma contagem e mosta na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return:sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end="...")
        c += p
    print("FIM!")


# Programa principal
contador(2, 20, 2)
help(contador)