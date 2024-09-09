cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print("\033[1;31mDeu um erro! Digite algo válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mO usuário descidiu não digitar nada!\033[m")
            return 0
        else:
            return n
def leiafloat(n):
    while True:
        try:
            n = float(input(n))
        except (ValueError, TypeError, AttributeError, KeyboardInterrupt):
            print("\033[1;31mHouve um erro,\033[1;33m tente mais uma vez!\033[m")
            continue
        else:
            return n
n1 = leiaInt("\033[1;37mDigite um número real:\033[1;32m ")
n2 = leiafloat("\033[1;37mDigite um número descimal:\033[1;32m ")
print(f"\033[1;34mA soma entre \033[1;32m{n1} \033[1;33m+ \033[1;32m{n2} \033[1;34mé \033[1;32m{n1 + n2}\033[1;34m!\033[m")
    
#print(f"{leiaInt("\033[1;37mIndique algo:\033[1;32m "), leiafloat("\033[1;37mIndique algo a mais:\033[1;32m ")}")



cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("Não foi possível acessar!")
else:
    print("tudo ok!")