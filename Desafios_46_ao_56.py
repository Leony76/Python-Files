from time import sleep
cores = {"limpa":"\033[m","azul":"\033[1;36m","amarelo":"\033[1;33m","verde":"\033[1;32m","roxo":"\033[1;35m","vermelho":"\033[1;31m","brancopreto":"\033[7;30m"}
print("{}₢=₢{}".format(cores["roxo"],cores["limpa"]) * 20) 
print("{}                 Contagem regressiva!!!{}".format(cores["verde"],cores["limpa"]))
print("{}₢=₢{}".format(cores["roxo"],cores["limpa"]) * 20) 
sleep(1)
for c in range(10,3,-1):
    sleep(1)
    print(cores["azul"],c)
for r in range(3,0,-1):
    sleep(1)
    print(cores["verde"],r)
sleep(1)
print(cores["vermelho"],0)
sleep(1)
print("{}AAAAAAAAEEEEEEEEEEEEEEEHHHHHHHHHHHHH!!!!!!!!!!{}".format(cores["vermelho"],cores["limpa"]))
