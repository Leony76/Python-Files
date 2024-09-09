print("O programa iniciou!")
n = int(input("Digite um número"))
print("O antecessor de {} é {} e seu sucessor é {}.".format(n,(n-1),(n+1)))




print("O programa iniciou!")
n = int(input("Digite um número"))
print("Seu dobro é {}! \nSeu triplo é {}! \nSua raiz é {}!".format((n*2),(n*3),pow(n,(1/2))))



print("O programa iniciou")
n1 = float(input("Digite uma nota"))
n2 = float(input("Digite outra nota"))
n3 = float(input("Digite mais uma nota"))
print("A média do aluno é {} ".format((n1+n2+n3)/3))

print("O progrma iniciou")
n1 = float(input("digite uma nota"))
n2 = float(input("Digite outra nota"))
n3 = float(input("Digite mais uma nota"))
m = (n1 + n2 + n3)/3
print("A média do aluno é {:.1f}.".format(m))
if m >= 7: print("Passou")
else: print("Não passou")

