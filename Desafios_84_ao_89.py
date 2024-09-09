
cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("\033[1;30mInsira o nome:\033[m ")))
    temp.append(float(input("\033[1;30mInsira o peso: Kg\033[m")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = str(input("\033[1;33mQuer continuar (s/n)\033[m")).strip().upper()[0]
    if cont in 'N':
        break
print(f"\033[1;36mVocê cadastrou \033[1;32m{princ}\033[m")
print(f"\033[1;36mO maior peso foi de \033[1;33m{mai}\033[1;36m!, os nomes são: \033[m", end='')
for p in princ:
    if p[1] == mai:
        print(f"\033[1;31m[{p[0]}]\033[m", end=' ')
print()
print(f"\033[1;36mO menor peso foi de \033[1;33m{men}\033[1;36m!, os nomes são: \033[m", end='')
for p in princ:
    if p[1] == men:
        print(f"\033[1;31m[{p[0]}]\033[m", end='')
print()
    
