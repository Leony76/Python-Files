cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
lista = []
maior = 0
menor = 0
continuar = ' '
while True:
    for i in range(0,5):
        lista.append(int(input("\033[1;30mDigite uma valor:\033[m ")))
        if i == 0:
            lista[i] = maior = menor
        else:
            if lista[i] > maior:
                maior = lista[i]
            elif lista[i]< menor:
                menor = lista[i]
    print(lista)
    print("\033[1;37mVocê digitou os números:\033[m ", end='')
    for v in lista:
        print(f"\033[1;32m{v}\033[m", end=' ')
    print(f"\n\033[1;34mO maior valor digitado foi \033[1;32m{maior}\033[1;34m, nas posições:\033[m", end=' ')
    for i, v in enumerate(lista):
        if v == maior:
            print(f"\033[1;33m{i+1}\033[m", end=' ')
    print()
    print(f"\033[1;34mO menor valor digitado foi \033[1;32m{menor}\033[1;34m, nas posições:\033[m", end=' ')
    for j, k in enumerate(lista):
        if k == menor:
            print(f"\033[1;33m{j+1}\033[m", end=' ')
    print()
    continuar = str(input("\033[1;35mDeseja continuar?: (s/n)\033[m ")).strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input("\033[1;35mDeseja continuar?: (s/n)\033[m ")).strip().upper()[0]
    if continuar in 'Nn':
        print("\033[1;31mPrograma encerrado!\033[m")
        break



