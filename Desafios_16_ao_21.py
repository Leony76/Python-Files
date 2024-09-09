import random
num = random.randint(1,10)
print(num)

from math import sqrt, floor
num = int(input("Insira um número: "))
raiz = sqrt(num)
print("A raiz de {} é igual a {}.".format(num,floor(raiz)))

from math import trunc
num = float(input("Insira um número: "))
print("Esse número inteiro equivale a {}.".format(trunc(num)))

import math
num = float(input("Insira um número flutuante: "))
print("O número flutuante {} equivale a {} em sua porção inteira!".format(num,math.trunc(num)))

num = float(input("Insira um núemro flutuante: "))
print("O número {} em sua inteira porção equivale a {}".format(num,int(num)))

from math import trunc
Co = float(input("Insira um cateto oposto: "))
Ca = float(input("Insira um cateto adjacente: "))
H = (Co**2 + Ca**2) ** (1/2)
print("O valor de {} e {} como catetos oposto e adjacente respectivamente equivalem a uma hipotenusa {}!".format(Co,Ca,trunc(H)))

from math import hypot, trunc
CO = float(input("Insira um cateto oposto: "))
CA = float(input("Insira um cateto adjacente: "))
H = hypot(CO,CA)
print("O cateto oposto {} e o cateto adjacente {} tem como hipotenusa {:.2f}!".format(CO,CA,trunc(H)))

Sen = float(input("Insira um ângulo: "))
Cos = float(input("Insira outro ângulo: "))
Tang = Sen / Cos
print("A tangente vale {:.2f}!".format(Tang))

import math
ang = float(input("Insira uma coisa: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print("O seno, cosseno e tangente desse número são, respectivamente: \n{:.2f} \n{:.2f} \n{:.2f}".format(seno,cosseno,tang))

import random
nome1 = str(input("Insira um nome: "))
nome2 = str(input("Insira outro nome: "))
nome3 = str(input("Insira outro nome: "))
nome4 = str(input("Insira mais um nome: "))
sorteio = [nome1,nome2,nome3,nome4]
escolhido = random.choice(sorteio)
print("O escolhido entre os 4 é o {}!".format(escolhido))

import random
nome1 = str(input("Insira um nome: "))
nome2 = str(input("Insira outro nome: "))
nome3 = str(input("Insira mais um nome: "))
nome4 = str(input("Insira mais um nome: "))
nome5 = str(input("Insira um último nome: "))
Lista = [nome1,nome2,nome3,nome4,nome5]
random.shuffle(Lista)
print("A ordem de apresentação será dada por: ")
print(Lista)










