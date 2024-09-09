for i in range(10,0, -1):
    print(i)

for i in range(0,10, 3):
    print(i)

n = int(input("Insira um núemro: "))
for i in range(0, n+1):
    print(i)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for l in range(i, f+1, p):
    print(l)

for i in range(0,3):
    n = int(input("Insira um valor: "))
print("FIM")

s = 0
for i in range(0,4):
    n = int(input("Insira um valor: "))
    s += n
print("O somatório desses núemros são {}.".format(s))

    