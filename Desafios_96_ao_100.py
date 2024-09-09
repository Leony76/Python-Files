cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
def área():
    L = int(input("\033[3;34m\033[1;34mIndique a Largura do terreno: "))
    C = int(input("\033[1;34mIndique o comprimento do terreno: "))
    A_Total = L * C
    print(f"\033[1;34mA área do terreno é de \033[1;33m{A_Total}m²\033[1;34m!\033[m")

área()