print("O programa iniciou")
n1 = int(input("Digite a largura da parede"))
n2 = int(input("Digite a altura da parede"))
n3 = int(input("Digite o comprimento"))
l = (n1*n2*n3)/2
print("A parede possui {}x{}x{} de área, com sua área de {}m³,sendo necessário L{} de tinta".format(n1,n2,n3,(n1*n2*n3),l))



print("O programa iniciou")
produto = int(input("Digite o preço do produto. R$"))
desconto = produto - (produto * 5/100)
print("O produto que custa R${} com 5% de desconto terá {}.".format(produto,desconto)) 




print("O programa iniciou")
Salario = int(input("Digite o salário do funcionário. R$"))
Aumento_de_reajuste = Salario + (Salario * 15/100)
print("O salario do funcionário de R${} passará a valer após o reajuste salarial,R${}.".format(Salario,Aumento_de_reajuste))



print("O programa iniciou")
Temp = float(input("Insira uma temperatura em °C:"))
Temp2 = float(input("Insira outra temperatura em °C:"))
Temp3 = float(input("Insira uma temperatura em °F:"))
Temp4 = float(input("Insira uma temperatura em °F:"))
Conversor = (Temp * 9/5) + 32
conversor2 = Temp2 + 273.15
conversor3 = (Temp3 - 32) * 5/9
conversor4 = (Temp4 - 32) * 5/9 + 273.15
print("{}°C equivale a {}°F. \n{}°C equivale a {}°K. \n{}°F equivale a {}°C. \n{}°F equivale a {}°K.".format(Temp,Conversor,Temp2,conversor2,Temp3,conversor3,Temp4,conversor4))



print("O prgrama iniciou")
QdD = int(input("Insira a quantidade de dias que usou o carro:"))
QdKm = float(input("Insira a quatidade de km's que rodou até o momento:"))
QdDaSP = QdD * 60
QdKmaSP = QdKm * 15/100
print("O valor do aluguel por {}dias usados e {}km(s) rodados será de {:.2f}.".format(QdD,QdKm,(QdDaSP + QdKmaSP)))