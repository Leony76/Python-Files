cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
cont = 0
n = 0
soma = 0
while True:
    n = int(input("{}Insira um valor aqui: {}".format(cores['vermelho'],cores['limpa'])))
    cont += 1
    if n == 999:
        break
    soma += n
print(f"Foram digitados \033[1;32m{cont}\033[m números, cujo os quais somados resultam em \033[1;32m{soma}!\033[m")


cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
n =  0
while True:
    n = int(input("\033[1;30mQuer ver qual tabuada?: \033[m"))
    if n < 0:
        print("\033[1;31mO programa foi cancelado!\033[m")
        break
    print("-=-" * 20)
    for i in range(1,11):
        print(f"\033[1;32m{n} \033[1;33mx \033[1;32m{i} \033[1;33m= \033[1;36m{n*i}\033[m")
    print("-=-" * 20)


cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
 
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
cont = 0
soma = 0
from random import randint
while True: 
    jogador1 = int(input("{}insira um número: {}".format(cores['cinza'],cores['limpa'])))
    jogador = str(input("\033[1;34mPar ou impar?: (P/I)\033[m")).upper().strip()[0]
    computador = randint(0,11)
    soma = jogador1 + computador
    if soma % 2 != 0:
        print(f"\033[1;36mVocê jogou \033[1;35m{jogador1}\033[1;36m, já o computador \033[1;35m{computador} \033[1;36me soma deles \033[1;32m'{soma}' \033[1;36mé impar!\033[m")
        if jogador in 'Ii':
            print("\033[1;32mVocê ganhou!\033[m")
            cont += 1
            if cont == 1:
                print(f"\033[1;33m{cont} vitória!\033[m")
            else:
                print(f"\033[1;33m{cont} vitórias!\033[m")
        else:
            if cont == 0:
                print(f"\033[1;31mVocê perdeu,com nenhuma vitória!\033[m") 
                break
            elif cont == 1:
                print(f"\033[1;31mVocê perdeu,com \033[1;33m{cont} \033[1;31mvitória apenas!\033[m")
            else:
                print(f"\033[1;31mVocê perdeu,com \033[1;33m{cont} \033[1;31mvitórias consecutivas!\033[m")
    else:
        print(f"\033[1;36mVocê escolheu \033[1;35m{jogador1}\033[1;36m, já o computador \033[1;35m{computador} \033[1;36me soma deles \033[1;32m'{soma}' \033[1;36mé par!\033[m")
        if jogador in 'Pp':
            print("\033[1;32mVocê ganhou!\033[m")
            cont += 1
            if cont == 1:
                print(f"\033[1;33m{cont} vitóra!\033[m")
            else:
                print(f"\033[1;33m{cont} vitórias!\033[m")
        else:
            if cont == 0:
                print(f"\033[1;31mVocê perdeu,com nehuma vitória!\033[m")
                break
            elif cont == 1:
                print(f"\033[1;31mVocê perdeu,com \033[1;33m{cont} \033[1;31mvitória apenas!\033[m")
            else:
                print(f"\033[1;31mVocê perdeu,com \033[1;33m{cont} \033[1;31mvitórias consecutivas!\033[m")
