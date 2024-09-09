
def contador(i,f,p):
    
    c = i
    while c <= f:
        print(f"{c}", end=' ')
        c += p
    print("END")

help(contador)

def soma(a=0,b=0,c=0):
    s = a + b + c
    print(f"A soma vale {s}")

soma()


def função():
    print(f"n1 local vale {n1}")

n1 = 2
print(f"n1 global vale {n1}")
função()

def soma_de_números(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = soma_de_números(1,2,3)
r2 = soma_de_números(4,6,32)
r3 = soma_de_números(543,2)

print(f"A soma dos números são respectivamente: {r1},{r2} e {r3}!")



def fatorial(núm=1):
    f = 1
    for i in range(núm,0,-1):
        f *= i
    return f

n = int(input("Digite um número: "))
print(f"O faorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(2)
f3 = fatorial(54)
f2 = fatorial(5)
print(f"O valor dos fatoriais são: {f1},{f2} e {f3}!")


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
number = int(input("insira um número: "))
print(par(number))

