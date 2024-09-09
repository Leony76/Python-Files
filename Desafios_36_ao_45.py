import time
Vcasa = float(input("Valor de casa: R$"))
Salário = float(input("Salário do palerma: R$"))
Qanos = int(input("Qauntos anos de financiamento?: "))
print("Calculando...")
time.sleep(1)
Prestação = Vcasa / (Qanos * 12)
Mínimo = Salário * 30/100
print("Para pagar uma casa de R${:.2f} em {} anos".format(Vcasa,Qanos), end=(' '))
print("a prestação será de R${:.2f}.".format(Prestação))
if Prestação <= Mínimo:
    print("O empréstimo pode ser concebido!")
else:
    print("Infelizmente o empréstimo não poderá ser concebido.")



 