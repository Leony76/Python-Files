def mostrarlinha():
    print("-----------------------------------------------")

mostrarlinha()
print(f"{'Programa iniciou':^45}")
mostrarlinha()

def mensagem(msg):
    print("-="*30)
    print(f"{msg:>30}")
    print("-="*30)

mensagem('Sistema de Mine')
mensagem('   Jogador')


a = 4
b = 5
s = a + b

a = 8
b = 9
s = a + b

def soma(a, b):
    s = a + b
    print(s)

soma(2, 4)
soma(8, 4)

def soma(c, d):
    print(f"A = {c} e B = {d}")
    s = c + d
    print(f"A soma de A + B resulta em {s}")

soma(d = 2, c = 4)
soma(7, 2)
soma(3, 5)





def contador(*núm):
    tam = len(núm)
    print(f"Foram {tam} números e são: ", end='')
    for i in núm:
        print(f"{i}", end=' ')
    print()


contador(5,7,3,1,4)
contador(8,4,7)
contador(5,7,8,0)

def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 6, 7, 8, 9]
dobrar(valores)
print(valores)


def soma(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f"Somando os valores {valores}, teremos {soma}")

soma(2, 4, 5, 6, 7)
soma(2, 5 ,6)

