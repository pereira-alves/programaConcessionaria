def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31mERRO, por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuario optou por não digitar um valor!')
            return 0
        else:
            return n


def linha(tam=50):
    return '~' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[31m{c} \033[m- \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[33mDigite uma opção: \033[m')
    return opc

def menuR(f,lista):
    cabeçalho(f'SEJA BEM VINDO A CONCESSIONÁRIA')
    c = 1
    for item in lista:
        print(f'\033[33m{f}\033[m.\033[31m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[33mDigite uma opção: \033[m')
    return opc
