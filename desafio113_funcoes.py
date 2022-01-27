def leiaint(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m")
      continue
    except (KeyboardInterrupt):
      print("\n\033[0;31mUsuário preferiu não digitar este número.\033[m")
      return 0
    else:
      return n


def leiafloat(msg):
  while True:
    n = str(input(msg)).replace(",", ".")
    try:
      n = float(n)
    except (ValueError, TypeError):
      print("\033[0;31mERRO! Por favor, digite um número real válido.\033[m")
      continue
    except (KeyboardInterrupt):
      print("\n\033[0;31mUsuário preferiu não digitar este número.\033[m")
      return 0
    else:
      n = str(n).replace(".", ",")
      return n
