"""
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado é {r}")
finally:
    print("Volte sempre! Muito obrigado!")
"""

"""-----------------------------------------------"""
"""
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito obrigado!")
"""
num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)
