dados = dict()
dados = {'Nome':'Pedro','Idade':'25'}
print(dados['Nome'])
print(dados['Idade'])
dados['sexo'] = 'M'
del dados['Idade']
print(dados)

filme ={'Título':'Star Wars',
        'Ano':'1977',
        'Diretor':'George Lucas'
        }
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f"O {k} é {v}!")


pessoas = {'Nomes':'Gustavo','Sexo': 'Masculino', 'Idade': 22}
print(f"O {pessoas['Nomes']} tem {pessoas['Idade']} anos, e é do sexo {pessoas['Sexo']}!")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']
pessoas['Nomes'] = 'Leandro'
pessoas['Peso'] = 54.6
for k,v in pessoas.items():
    print(f"{k} = {v}")

estado = {'UF':'Rio de Janeiro','Sigla':'RJ'}
esdado2 = {'UF':'São Paulo','Sigla':'SP'}
brasil = []
brasil.append(estado)
brasil.append(esdado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['Sigla'])

Estado = dict()
Brasil = list()
for c in range(0,3):
    Estado['UF'] = str(input("Unidade Federativa: "))
    Estado['Sigla'] = str(input("Sigla do estado: "))
    Brasil.append(Estado.copy())
print(Brasil)
for e in Brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()
