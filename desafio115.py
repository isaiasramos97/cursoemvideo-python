"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""


def titulo(txt):
    tam = len(txt * 3)
    print("-" * tam)
    print(f"{' ' * len(txt)}{txt}{' ' * len(txt)}")
    print("-" * tam)


def mostralinha():
    print("-" * 42)


def opcao():
    try:
        opt = int(input("Sua Opção: "))
    except:
        print("Por favor, digite um número inteiro válido.")
    else:
        


titulo("MENU PRINCIPAL")
print("1 - Ver pessoas cadastradas\n"
      "2 - Cadastrar nova Pessoa\n"
      "3 - Sair do Sistema")
mostralinha()
