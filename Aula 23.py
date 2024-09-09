#n = int(input("Insira um comando: "))
#print(f"Você digitou {float(n)}!")

#n = int(input("Insira um número: "))
#print(f"Você digitou {n}")

#a = int(input("Primeiro valor: "))
#b = int(input("Insira um valor: "))
#f = a / b
#print(float(f))

try:
    a = int(input("Insira um valor: "))
    b = int(input("Insira outro valor: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos alguns problemas com o que você digitou!")
except ZeroDivisionError:
    print("Não é possível divisão por zero!")
except KeyboardInterrupt:
    print("Não foi informado nenhum número!")
else:
     print(f"{a} / {b} = {r}")
finally:
    print("Volte sempre!")