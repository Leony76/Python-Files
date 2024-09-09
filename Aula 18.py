dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #Pedro
print(dados[1]) #25

pessoas = list()
pessoas.append(dados[:])
              #0    #1  |  #0   #1  |   #0   #1
pessoas = [['Pedro',25],['Maria',19],['João',32]]
                 #0           #1           #2
print(pessoas[0][0]) #Pedro
print(pessoas[2][0]) #João
print(pessoas[1][1]) #19
print(pessoas[1]) #['Maria', 19]

teste = list()
teste.append('Leony')
teste.append(18)
print(teste)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p[1])
for p in galera:
     print(f"{p[0]} tem {p[1]} anos de idade!")

galera1 = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,2):
     dado.append(str(input("Nome: ")))
     dado.append(int(input("Idade: ")))
     galera1.append(dado[:])
     dado.clear()
print(f"{galera1}")
for p in galera1:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade!")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade!")
        totmenor += 1
print(f"Temos {totmaior} maiores de idade e {totmenor} menores de idade!")
