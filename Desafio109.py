def metade(n=0, format=False):
    return n / 2 if not format is False else moeda(n /2)
def dobro(n=0, format=False):
    return n * 2 if not format is False else moeda(n / 2)
def aumentar(n=0, format=False):
    return n + (n * 0.10) if not format is False else moeda(n+(n*0.1))
def diminuir(n=0, format=False):
    return n - (n* 0.13) if not format is False else moeda(n-(n*0.13))
def moeda(preço=0,moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.',',')