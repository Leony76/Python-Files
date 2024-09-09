n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Foram {} pares e {} impares indicados!".format(par,impar))

n = 1
while n != 0:
    n = int(input("Insira algo: "))
print("Fim")

r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar?: (S/N) ")).upper()
print("FIm")

idade = 0
while idade < 18:
    idade = int(input("Insira uma idade: "))
print("fim")

