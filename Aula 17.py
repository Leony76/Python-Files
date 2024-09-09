num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
    num.remove(4)
else:
    print("Não há número 4")
print(num)
print(f"Essa lista tem {len(num)} elementos")



valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for j,v in enumerate(valores):
   print(f"Na posição {j}, encontrei o valor {v}!")
print("Cheguei na lista final!")



Values = list()
for cont in range(0,5):
    Values.append(int(input("Digite um valor: ")))
print(Values)
for i, j in enumerate(Values):
    print(f"Na posição {i+1}, está o nº {j}")



a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")