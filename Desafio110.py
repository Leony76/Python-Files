def dobro(n):
    res = n * 2
    return res
def metade(n):
    res = n / 2
    return res




def moeda(p=0, aumento=0, redução=0):
    print(f"\033[1;34mO valor analisado é \033[1;32mR${p:.2f}\033[1;34m!".replace('.',','))
    print(f"\033[1;34mO \033[1;33mdobro \033[1;34mde \033[1;32mR${p:.2f} \033[1;34mé igual a \033[1;32mR${dobro(p):.2f}\033[1;34m!".replace('.',','))
    print(f"\033[1;34mA \033[1;33mmetade \033[1;34mde \033[1;32mR${p:.2f} \033[1;34mé igual a \033[1;32mR${metade(p):.2f}\033[1;34m!".replace('.',','))
    print(f"\033[1;34mO \033[1;33maumento \033[1;34mde \033[1;33m{aumento}% \033[1;34msobre \033[1;32mR${p:.2f} \033[1;34mequivale a \033[1;32mR${(p + (p * aumento//100)):.2f}\033[1;34m!".replace('.',','))
    print(f"\033[1;34mA \033[1;33mredução \033[1;34mde \033[1;33m{redução}% \033[1;34msobre \033[1;32mR${p:.2f} \033[1;34mequivale a \033[1;32mR${(p - (p * redução//100)):.2f}\033[1;34m!\033[m".replace('.',','))