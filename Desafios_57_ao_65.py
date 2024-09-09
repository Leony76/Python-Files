cores = {"limpa":"\033[m","azul":"\033[1;36m","amarelo":"\033[1;33m","verde":"\033[1;32m","roxo":"\033[1;35m","vermelho":"\033[1;31m","brancopreto":"\033[7;30m"}
print("{}₢=₢{}".format(cores["roxo"],cores["limpa"]) * 20) 
print("{}                   O PROGRAMA INCIOU!{}".format(cores["verde"],cores["limpa"]))
print("{}₢=₢{}".format(cores["roxo"],cores["limpa"]) * 20)
Sexo = str(input("Informe o sexo da pessoa: [M/F]")).strip().upper()[0]
while Sexo not in 'MF':
    print("Desculpe, informe apenas M ou F, por favor.")
    Sexo = str(input("Informe o sexo da pessoa: [M/F]")).strip().upper()[0]
print("Validação feita com sucesso!")

from random import randint
cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
computador = randint(0,10)
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}Sou seu computador.. Acabei de pensar em um núemro. Consegue advinhar?{}".format(cores['amarelo'],cores['limpa']))
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("{}Qual é seu palpite?:{} ".format(cores['azul'],cores['limpa'])))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("{}Quase, um pouco mais{}".format(cores['vermelho'],cores['limpa']))
        elif jogador > computador:
            print("{}Quase, um pouco menos{}".format(cores['vermelho'],cores['limpa']))
print("{}-=-{}".format(cores['azul'],cores['limpa']) * 27)
print("{}Acertô miseraví... na {}ª{}".format(cores['verde'],palpites,cores['limpa']))
print("{}-=-{}".format(cores['azul'],cores['limpa']) * 27)

cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print()
import time
n1 = int(input("{}Digite um número:{} ".format(cores['cinza'],cores['limpa'])))
n2 = int(input("{}Digite outro número:{} ".format(cores['cinza'],cores['limpa'])))
print()
print("{}O que você deseja com {} e {}?{}".format(cores['amarelo'],n1,n2,cores['limpa']))
print()
print("{}[ 1 ] Somar{}".format(cores['azul'],cores['limpa']))
print("{}[ 2 ] Multiplicar{}".format(cores['azul'],cores['limpa']))
print("{}[ 3 ] Maior entre{}".format(cores['azul'],cores['limpa']))
print("{}[ 4 ] Digitar novos números{}".format(cores['roxo'],cores['limpa']))
print("{}[ 5 ] Encerrar o programa{}".format(cores['vermelho'],cores['limpa']))
escolha = int(input(": "))
if escolha == 1:
    print("{}A soma entre {} e {} é igual a {}!{}".format(cores['verde'],n1,n2,(n1+n2),cores['limpa']))
elif escolha == 2:
    print("{}O produto entre {} e {} é igual a {}!{}".format(cores['verde'],n1,n2,(n1*n2),cores['limpa']))
elif escolha == 3:
    maior = n1
    if n2 > n1:
        maior = n2
        print("{}O maior entre {} e {} é o {}!{}".format(cores['verde'],n1,n2,maior,cores['limpa']))
    elif n1 == n2:
        print("{}Ambos os números são iguais!{}".format(cores['verde'],cores['limpa']))
while escolha == 4:
    print()
    print("{}Certo, escolha novos números!{}".format(cores['amarelo'],cores['limpa']))
    print()
    n1 = int(input("{}Digite um número:{} ".format(cores['cinza'],cores['limpa'])))
    n2 = int(input("{}Digite outro número:{} ".format(cores['cinza'],cores['limpa'])))
    print()
    print("{}O que você deseja com {} e {}?{}".format(cores['amarelo'],n1,n2,cores['limpa']))
    print()
    print("{}[ 1 ] Somar{}".format(cores['azul'],cores['limpa']))
    print("{}[ 2 ] Multiplicar{}".format(cores['azul'],cores['limpa']))
    print("{}[ 3 ] Maior entre{}".format(cores['azul'],cores['limpa']))
    print("{}[ 4 ] Digitar novos números{}".format(cores['roxo'],cores['limpa']))
    print("{}[ 5 ] Encerrar o programa{}".format(cores['vermelho'],cores['limpa']))
    escolha = int(input(": "))
    if escolha == 1:
        print("{}A soma entre {} e {} é igual a {}!{}".format(cores['verde'],n1,n2,(n1+n2),cores['limpa']))
    elif escolha == 2:
        print("{}O produto entre {} e {} é igual a {}!{}".format(cores['verde'],n1,n2,(n1*n2),cores['limpa']))
    elif escolha == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print("{}O maior entre {} e {} é o {}!{}".format(cores['verde'],n1,n2,maior,cores['limpa']))
    elif escolha == 5:
        print("{}Encerrando...{}".format(cores['amarelo'],cores['limpa']))
        time.sleep(2)
        print("{}Programa encerrado!{}".format(cores['vermelho'],cores['limpa']))
    else:
        print("{}Número inválido, digite um dos 5:{}".format(cores['vermelho'],cores['limpa']))
if escolha == 5:
    print("{}Encerrando...{}".format(cores['amarelo'],cores['limpa']))
    time.sleep(2)
    print("{}Programa encerrado!{}".format(cores['vermelho'],cores['limpa']))
else:
    print("{}Número inválido, digite um dos 5:{}".format(cores['vermelho'],cores['limpa']))

