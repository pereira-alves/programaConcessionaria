from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivoCliente(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('CONSULTA')
        for key, value in enumerate(a):
            dado = value.split(';')
            dado[3] = dado[3].replace('\n', '')
            print(f'Chave = \033[31m{key}\033[m --- IdCliente:\033[31m{dado[0]:<5}\033[mNome: \033[31m{dado[1]:<30}\033[mCPF: \033[31m{dado[2]:<15}\033[mTelefone: \033[31m{dado[3]:>10}\033[m')
    finally:
        a.close()


def lerArquivoMoto(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('CONSULTA')
        for key, value in enumerate(a):
            dado = value.split(';')
            dado[2] = dado[2].replace('\n','')
            print(f'Chave = \033[31m{key}\033[m --- Modelo: \033[31m{dado[0]:<20}\033[m Ano:\033[31m{dado[1]:<5}\033[m Situação: \033[31m{dado[2]:<10}\033[m')
    finally:
        a.close()


def lerArquivoMotoCopia(nome):
    try:
        a = open(nome, 'r+')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('EM ESTOQUE')
        for key, value in enumerate(a):
            dado = value.split(';')
            dado[2] = dado[2].replace('\n','')
            if dado[2] == ' Disponivel':
                print(f'Chave = \033[31m{key}\033[m Modelo: \033[31m{dado[0]:<20}\033[m Ano:\033[31m{dado[1]:<15}\033[m Situação: \033[31m{dado[2]:>10}\033[m')
    finally:
        a.close()


def lerArquivoMotoVenda(nome):
    try:
        a = open(nome, 'r+')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('VENDIDO')
        for key, value in enumerate(a):
            dado = value.split(';')
            dado[5] = dado[5].replace('\n','')
            print(f'Venda nº \033[31m{key}\033[m --- Cliente \033[31m{dado[0]}\033[m -\033[31m{dado[1]}\033[m - CPF: \033[31m{dado[2]}\033[m / Compra do Veículo: \033[31m{dado[3]}\033[m -\033[31m{dado[4]}\033[m ano\033[31m{dado[5]}\033[m')
    finally:
        a.close()


def cadastrarCliente(arq, idcliente, nome='desconhecido', cpf=0, telefone=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{idcliente};{nome};{cpf};{telefone}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def cadastrarMoto(arq, modelo='desconhecido', ano=0, situ='Indisponivel'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{modelo}; {ano}; {situ}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {modelo} adicionado.')


# with is like your try .. finally block in this case
def substituirCliente(chave, idcliente,nome='desconhecido', cpf=0, telefone=0):
    with open('cliente.txt', 'r') as file:
        data = file.readlines()  # read a list of lines into data
    data[chave] = f'{idcliente};{nome};{cpf};{telefone}\n' # agora vamos trocar a linha do arquivo que será identificada pela chave
    with open('cliente.txt', 'w') as file: # and write everything back
        file.writelines(data)
    print(f'Alterações de dados de {nome} feita com sucesso!')


def substituirMoto(chave,modelo, ano, situ):
    with open('motos.txt', 'r') as file:
        data = file.readlines() # read a list of lines into data
    data[chave] = f'{modelo}; {ano}; {situ}\n'  # agora vamos trocar a linha do arquivo que será identificada pela chave
    with open('motos.txt', 'w') as file: # and write everything back
        file.writelines(data)
    print(f'Alterações de dados para {modelo} feita com sucesso!')


def cadastrarVenda(arq, idcliente, nome, cpf, chave, modelo, ano):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{idcliente}; {nome}; {cpf}; {chave}; {modelo}; {ano}\n')
        except:
            print('Hoube um ERRO na hora de registrar a venda!')
        else:
            a.close()


def substituirVenda(item, idcliente, nome, cpf, chave, modelo, ano):
    with open('venda.txt', 'r') as file:
        data = file.readlines() # read a list of lines into data
    data[item] = f'{idcliente}; {nome}; {cpf}; {chave}; {modelo}; {ano}\n'  # agora vamos trocar a linha do arquivo que será identificada pela chave
    with open('venda.txt', 'w') as file: # and write everything back
        file.writelines(data)
    print(f'Alterações de dados para feita com sucesso!')


def removerMoto(arq,chave,nova_linha):
    with open(arq,'r') as f:
        texto=f.readlines()
    with open(arq,'w') as f:
        for i in texto:
            if texto.index(i)==chave:
                f.write(nova_linha+'\n')
            else:
                f.write(i)
    print(f'Chave {chave} removida com sucesso!')


def removerVenda(arq,chave,nova_linha):
    with open(arq,'r') as f:
        texto=f.readlines()
    with open(arq,'w') as f:
        for i in texto:
            if texto.index(i)==chave:
                f.write(nova_linha+'\n')
            else:
                f.write(i)
