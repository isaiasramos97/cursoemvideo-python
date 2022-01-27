from ex115.lib.arquivo import *
from ex115.lib.interface import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do sistema"])
    if resp == 1:
        # Opção para listar o conteúdo do arquivo
        lerarquivo(arq)
    elif resp == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho("Saindo do sistema... até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
