
def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print("\033[1;31mDeu um erro! Digite algo válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mO usuário descidiu não digitar nada!\033[m")
            return 0
        else:
            return n
        
def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[1;33m{c}\033[m - \033[1;34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[1;35mSua Opção:\033[m ")
    return opc
