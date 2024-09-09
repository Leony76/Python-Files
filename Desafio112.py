def dobro(n):
    dobro = n * 2
    return dobro
def metade(n):
    metade = n / 2
    return metade

def leiacorreto(n):
    válido = False
    while not válido:
        entrada = str(input(n))
        if entrada.isalpha():
            print(f"\033[1;31mERRO! \033[1;33m{entrada} \033[1;31mé um preço inválido!\033[m")
        if entrada == "":
            print(f"\033[1;31mERRO! \033[1;33m<NONE> \033[1;31mé um preço inválido!\033[m")
        else:
            válido = True
            return int(entrada)

def dinheiro(n,aumento=0,redução=0):
    print("\033[1;36m~"*56)
    print(f"\033[1;35m{'Analise de Moeda':^56}")
    print("\033[1;36m~"*56)
    print(f"  \033[1;33mValor:                                        \033[1;32mR${n:.2f}\033[m".replace('.',','))
    print(f"  \033[1;33mDobro do Valor:                               \033[1;32mR${dobro(n):.2f}\033[m".replace('.',','))
    print(f"  \033[1;33mMetade do Valor:                              \033[1;32mR${metade(n):.2f}\033[m".replace('.',','))
    print(f"  \033[1;33m{aumento}% de Aumento sobre o Valor:                 \033[1;32mR${(n + (n * aumento//100)):.2f}\033[m".replace('.',','))
    print(f"  \033[1;33m{redução}% de redução sobre o Valor:                 \033[1;32mR${(n - (n * redução//100)):.2f}\033[m".replace('.',','))
    print("\033[1;36m~\033[m"*56)

