nome = str(input("Qual seu nome ")).strip()
if nome == "Lerico":
    print("Esse é o cara!")
elif nome == "Khrarah" or nome == "Yoturoo" or nome == "Gontch":
    print("Você é um Ehlárce, boa...")  
elif nome in "Pedro, Issac, Arthur":
    print("Achei que fosse outro...")
else:
    print("Seu nome é normal...")
print("Tenha um boma dia!".format(nome))