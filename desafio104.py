def LeiaInt(msg):
  ok = False
  valor = 0
  while True:
    n = str(input(msg)).strip()
    if n.isnumeric():
      valor = int(n)
      ok = True
      break
    print("\033[0;31mERRO! Digite um número inteiro.\033[m")
  return valor


n = LeiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")