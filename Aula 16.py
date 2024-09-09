lanche = ("Hambúrguer", "Suco", "Torta", "Pudim")
for pos,comida in enumerate(lanche):
    print(f"Comerei {comida} na posição {pos+1}")


for cont in range(0, len(lanche)):
    print(lanche[cont])
    print(cont+1)


for comida in lanche:
    print(f"Eu comerei {comida}")
    if comida in 'Suco':
        print(f"Eu beberei Suco")


print(sorted(lanche))


a = (2, 5, 4)
b = (6, 7, 8)
c = a + b
print(c)
print(c.index(7+1))



