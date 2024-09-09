cont = ('zero','um','dois','três','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze',
        'quatorze','quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
continuar = ' '
while True:
    núm = int(input("Insira um número entre 0 e 20: "))
    if 0 <= núm <= 20:
        print("Tente novamente", end=',')
    else:
        print(f"Você digitou o número {cont[núm]}")
    while continuar not in 'SN':
        continuar = str(input("Quer continuar?: (s/n)")).strip().upper()[0]
    if continuar in 'Nn':
        break


lista = ['Atlético-PR','Bahia','Flamengo','Botafogo','São Paulo','Cruziero',
         'Atlético-MG','Bragantino','Palmeiras','Internacional','Fortaleza',
         'Grêmio','Vasco da Gama','Criciúma','Juventude','Corínthians','Fluminense',
         'EC Vitória','Atlético-GO','Cuiabá']
print(f"Lista de de times: \033[1;32m{lista}\033[m", end='|')

for times in lista:
    print(times)

print(f"Os 5 primeiros times são: \033[1;32m{lista[0:5]}\033[m")
print()
print(f"Os últimos colocados são: \033[1;31m{lista[-4:]}\033[m")
print()
print(f"Os time em ordem alfabética são listadas como: \033[1;33m{sorted(lista)}\033[m")
print()
print('O flamengo está na posição {}'.format(lista.index('Flamengo')))


from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),
     randint(1,10),randint(1,10),)
print(f"Os números sorteados foram:",end=' ' )
for n in numeros:
    print(f"{n}",end=' ')
print(f"\nO maior valor citado foi: {max(numeros)}")
print(f"O menor valor citado foi: {min(numeros)}")
    

cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
lista = []
cont = ' '
lista_par = []
while True:
    n = int(input("\033[1;30mInsira um número: \033[m"))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    cont = str(input("\033[1;34mDeseja continuar?: (s/n)\033[m")).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input("\033[1;34mDeseja continuar?: (s/n)\033[m")).strip().upper()[0]
    if cont in 'Nn':
        break
print(f"\033[1;33mVocê digitou os números:\033[m", end=' ')
for num in lista:
    print(f"\033[1;32m{num}\033[m",end=' ')
print(f"\n\033[1;34mO número \033[1;33m9 \033[1;34mfoi citado \033[1;32m{lista.count(9)} \033[1;34mvezes\033[m")
if 3 in lista:
    print(f"\n\033[1;34mO nº \033[1;33m3 \033[1;34mfoi citado na posição \033[1;32m{(lista.index(3))+1}\033[m")
print("\033[1;34mOs números pares citados foram:\033[m", end=' ')
for num1 in lista_par:
    print(f"\033[1;32m{num1}\033[m", end=' ')


cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
listagem = ['Lápis', 1.75, 
            'Borracha',2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Copasso', 9.90,
            'Mochila', 120.35,
            'Canetas', 22.30,
            'Livro', 34.90]
print(f"{'Listagem de preços':^40}")
for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f"\033[1;33m{listagem[item]:.<30}\033[m", end='')
    else:
        print(f"\033[1;32mR${listagem[item]:>7.2f}\033[m")


cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 20)
lista = ['Abacaxi',
         'Borracha',
         'Carro',
         'Defesa',
         'Escola',
         'Falso',
         'Ganho',
         'Hotel',
         'Igreja',
         'Jogo',
         'Khrarah',
         'Lerico']
for listagem in lista:
    print(f"\n\033[1;34mNa palavra \033[1;33m{listagem.upper()}\033[1;34m, temos:\033[m", end=' ')
    for letra in listagem:
        if letra.lower() in 'aeiou':
            print(f"\033[1;32m{letra}\033[m" , end=' ')













 
