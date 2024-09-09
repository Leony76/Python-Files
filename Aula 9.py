frase = "Lerico.T.Chesky"
print(frase[7])

frase = "Lerico.T.Chesky"
print(frase[9:16])

frase = "Lerico.T.Chesky"
print(frase[:7])

frase = "Lerico.T.Chesky"
print(frase[3:])

frase = "Lerico.T.Chesky"
print(frase[2:13:3])

frase = "Lerico.T.Chesky"
print(frase[::4])

frase = "Lerico.T.Chesky"
print(frase.count('i'))
print(frase.count('o'))

frase = "Lerico.T.Chesky"
print(frase.upper().count("E"))

frase = "  Lerico.T.Chesky     "
print(len(frase))
print(len(frase.strip()))
print(len(frase.rstrip()))
print(len(frase.lstrip()))

frase = "Lerico.T.Chesky"
print(frase.replace("Lerico","Khrarah"))
frase = "Lerico.T.Chesky"
print(frase.replace(".T."," "))
frase = "Lerico.T.Chesky"
print(frase.replace("Chesky","Layanne"))

frase = "Lerico.T.Chesky"
print(frase.find("Lerico"))

frase = "Lerico.T.Chesky"
print(frase.upper().find("CHESKY"))

frase = "LERICO.T.CHESKY"
print(frase.lower().find("chesky"))

frase = "Lerico Tenebras Chesky"
print(frase.split())

frase = "Lerico. T .Chesky"
dividido = frase.split()
print(dividido[2])

frase = "Lerico. T .Chesky"
dividido = frase.split()
print(dividido[2][5])





