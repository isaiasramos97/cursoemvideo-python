# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://loja.fluminense.com.br/")
except urllib.error.URLError:
    print("O site Loja Fluminense não está acessível no momento!")
else:
    print("O site Loja Fluminense está acessível!")
    # print(site.read()) lê o código do site
