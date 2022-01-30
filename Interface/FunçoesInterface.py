def linha(tam=30):
    return '-'*tam

def cabeçalho(txt):
    print(linha(30))
    print(txt.center(30))
    print(linha(30))

def leiaint(a):
    while True:
        try:
            i=int(input(a))
        except (ValueError,TypeError):
            print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mUsuario preferiu não digitar esse numero.\033[m')
            return 0
        else:
            return i

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc
