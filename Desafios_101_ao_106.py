import datetime

cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)

while True:
    def voto(núm=2024):
        idade = datetime.date.today().year - núm
        if idade < 16:
            print(f"\033[4;m\033[1;34mCom \033[1;33m{idade} \033[1;34manos, você ainda não pode votar, pois faltam \033[1;33m{18-idade} \033[1;34manos ainda!")
        elif 16 <= idade < 18:
            print(f"\033[1;34mCom \033[1;33m{idade} \033[1;34manos, você já pode votar, porém é opcional, sendo obrigatório em \033[1;33m{18-idade} \033[1;34manos!") 
        elif 18 <= idade < 65:
            print(f"\033[1;34mCom \033[1;34m{idade} \033[1;34manos, você tem obrigação de votar, tornado apenas opcional aos \033[1;31m65 anos\033[1;34m, ou em \033[1;33m{65-idade} \033[1;34manos!")    
        else:
            print(f"\033[1;34mCom \033[1;33m{idade} \033[1;34manos, você não tem mais obrigação de votar, pois já passou dos \033[1;31m65 anos\033[1;34m a \033[1;33m{idade-65} \033[1;34manos!")    
        return idade

    I = int(input("\033[1;37mEm que ano nasceu?: "))
    voto(I)
    cont = str(input("\033[1;35mQuer continuar?: (S/N)")).strip().upper()[0]
    if cont in 'N':
        break



cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)

def ficha(nome="\033[1;31m<desconehcido>\033[m",gols=0):
    print(f"\033[1;34mO jogador \033[1;33m{nome} \033[1;34mfez \033[1;33m{gols} \033[1;34mgols no campeonato!\033[m")

n = str(input("\033[1;37mInsira o nome do jogador: "))
gol = str(input("Insira o número de gols que ele marcou: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if n.strip() == '':
    ficha(gols=gol)
else:
    ficha(n,gol)



cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
def numInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input("\033[1;37mInsira um número: "))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;31mERRO! Digite um valor válido")
        if ok == True:
            break
    return valor

n = numInt("\033[1;37mInsira um número: ")
print(f"\033[1;34mVocê citou o número \033[1;33m{n}\033[1;34m!\033[m")



cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
def notas(*n, sit=False):
    Notas = dict()
    Notas['Quantidade de notas'] = len(n)
    Notas['Maior nota'] = max(n)
    Notas['Menor nota'] = min(n)
    Notas['Média das notas'] = sum(n)/len(n)
    print(Notas)
    if sit:
        if Notas['Média das notas'] >= 7:
            return print("\033[1;32mA situação é boa!\033[m")
        elif 4 < Notas['Média das notas'] < 7:
            return print("\033[1;33mA situação está razoável!\033[m")
        else:
            return print("\033[1;31mA situação está bem ruim!\033[m")
        
notas(10,10,10, sit=False)



cores = {'limpa':'\033[m','azul':'\033[1;36m','vermelho':'\033[1;31m','verde':'\033[1;32m','amarelo':'\033[1;33m','azul escuro':'\033[1;34','roxo':'\033[1;35m','cinza':'\033[1;37m'}
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)
print("{}                         O PROGRAMA INICIOU !!!{}".format(cores['roxo'],cores['limpa']))
print("{}₢==₢{}".format(cores['verde'],cores['limpa']) * 19)

c = ('\033[m',         
     '\033[0;37;41m',  
     '\033[0;37;42m',  
     '\033[0;37;43m',  
     '\033[0;37;44m',  
     '\033[0;37;45m',  
     '\033[7;30m'
    );
    


def helpfunção(n):
    título(f"Acessando o manual do comando \'{n}\'", 4)
    print(c[6], end='')
    help(n)
    print(c[0], end='')

def título(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("=" * tam)
    print(f"{msg}")
    print("="* tam)
    print(c[0], end='')


while True:
    título("Sistema de ajuda Pyhelp",2)
    resp = str(input("\033[1;37mInsira uma função:\033[m "))
    helpfunção(resp)
    cont = str(input("\033[1;33mContinuar? (S/N)\033[m")).strip().upper()[0]
    if cont in 'N':
        título("Até logo!!!", 1)
        break




