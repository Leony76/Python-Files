import random
a = int(input("Digite um número entre 0 e 5: "))
lista = [0,1,2,3,4,5]
emb = random.choice(lista)
print("O número escolhido foi {}!".format(emb))
if a == emb:
    print("Você acertou!")
else:
    print("Você errou!")

from random import randint
from time import sleep
c = randint(0,5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5.Tente advinhar!")
print("-=-" * 20)
player = int(input("Em que número pensei? "))
print("processando...")
sleep(2)
if player == c:
    print("Boa!")
else:
    print("Você errou!Eu pensei no número {} e você no número {}...".format(c,player))

V = int(input("Qual velocidade o motorista percorreu no trajeto?: "))
m = (V - 80) * 7 
if V > 80:
    print("Você foi multado!, terá que pagar R${} pela mesma!".format(m))
    print("Dirija com mais cutela próxima vez!")
else:
    print("Tenha um bom dia!")


from time import sleep
dist = int(input("Insira a quantidede de kms que você viajará: "))
VC = dist * 0.50
VL = dist * 0.45
print("Calculando...")
sleep(2)
if dist <= 200:
    print("A viajem te custará R${:.2f}!".format(VC))
else:
    print("A viajem com exedente de 200km te custará apenas R${:.2f}!".format(VL))

dist = int(input("Insira a quantidade de kms que você viajará: "))
print("Você está prestes a ter uma viajem de {}kms!".format(dist))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print("O preço de sua viajem será de R${}!".format(preço))

N = int(input("Digite um núemro: "))
if N % 2 == 0:
    print("É par")
else:
    print("É ímpar")

from datetime import date
ano = int(input("Insira um ano para ser analisado: "))
if ano == 0:
    ano = date.today().year   
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto!".format(ano))
else:
    print("Não é Bissexto!")

a = int(input("Insira um número: "))
b = int(input("Insira outro núemro: "))
c = int(input("Insira um último número: "))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print("o menor número ditado foi o {}!".format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O maior número ditado é o {}!".format(maior))
    








