from lib.interface import *
from lib.arquivo import *
from time import sleep
from random import randint

arqCliente = 'cliente.txt'
if arquivoExiste(arqCliente):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arqCliente)
arcMotos = 'motos.txt'
if arquivoExiste(arcMotos):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arcMotos)

arcVenda = 'venda.txt'
if arquivoExiste(arcVenda):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arcVenda)


while True:
    resposta = menu(['MENU CLIENTES', 'MENU MOTOCICLETAS', 'SISTEMA DE VENDAS', 'SAIR'])
    if resposta == 1:
        while True:
            resposta = menuR(resposta, ['CADASTRAR NOVO CLIENTE', 'ALTERAR DADOS','CONSULTAR LISTA DE CLIENTES','VOLTAR AO MENU'])
            if resposta == 1:
                cabeçalho('NOVO CADASTRO')
                idcliente = []
                idcliente.append(randint(1,100))
                idcliente.append(str(input('Nome: ')).upper())
                idcliente.append(leiaint('CPF: '))
                idcliente.append(leiaint('Telefone: '))
                cadastrarCliente(arqCliente, idcliente[0], idcliente[1], idcliente[2], idcliente[3])
            elif resposta == 2:
                lerArquivoCliente(arqCliente)
                chave = leiaint('Qual chave deseja alterar ?')
                idcliente = leiaint('Informe o Idcliente: ')
                nome = str(input('Novo Nome: ').upper())
                cpf = leiaint('Novo CPF: ')
                telefone = leiaint('Novo Telefone: ')
                substituirCliente(chave, idcliente, nome, cpf, telefone)
            elif resposta == 3:
                lerArquivoCliente(arqCliente)
            elif resposta == 4:
                break
            else:
                print('Digite uma opção válida!')
    elif resposta == 2:
        while True:
            resposta = menuR(resposta,['CADASTRO DE NOVA MOTOCICLETA', 'ALTERAÇÃO DE CADASTRO', 'REMOVER MOTOCICLETA', 'VOLTAR AO MENU'])
            if resposta == 1:
                modelo = str(input('Modelo: ')).upper()
                ano = leiaint('Ano: ')
                print('Situação: 1 - Disponivel / 2 - Vendido')
                while True:
                    situ = leiaint('Opção: ')
                    if situ == 1:
                        situ = 'Disponivel'
                        break
                    elif situ == 2:
                        situ = 'Vendido'
                        break
                    else:
                        print('Escolha uma opção válida!')
                cadastrarMoto(arcMotos, modelo, ano, situ)
            elif resposta == 2:
                lerArquivoMoto(arcMotos)
                chave = leiaint('Qual chave deseja alterar ?')
                modelo = str(input('Modelo: ').upper())
                ano = leiaint('Ano: ')
                print('Situação: 1 - Disponivel / 2 - Vendido')
                while True:
                    situ = leiaint('Opção: ')
                    if situ == 1:
                        situ = 'Disponivel'
                        break
                    elif situ == 2:
                        situ = 'Vendido'
                        break
                substituirMoto(chave, modelo, ano, situ)
            elif resposta == 4:
                break
            elif resposta ==3:
                lerArquivoMoto(arcMotos)
                chave = leiaint('Qual chave deseja remover ? ')
                nova_linha = 'REMOVIDO ;REMOVIDO ;REMOVIDO'
                removerMoto(arcMotos, chave, nova_linha)
            else:
                print('Digite uma opção válida!')

    elif resposta == 3:
        while True:
            resposta = menuR(resposta, ['CONSULTA DE MODELOS','EFETUAR VENDA', 'ALTERAÇÃO DE DADOS PARA VENDAS'
                                              ' EFETUADAS', 'CONSULTAR VENDAS','CANCELAR VENDA', 'VOLTAR AO MENU'])
            if resposta == 1:
                lerArquivoMoto(arcMotos)
            elif resposta == 2:
                cabeçalho('INICIANDO SISTEMA DE VENDA')
                lerArquivoCliente(arqCliente)
                print('DADOS DO CLIENTE')
                idcliente = leiaint('Id do cliente: ')
                nome = str(input('Nome do Cliente: ').upper())
                cpf = leiaint('CPF: [APENAS NÚMEROS]')
                lerArquivoMotoCopia(arcMotos)
                print('DADOS DO VEÍCULO')
                chave = leiaint('Chave de Identificação: ')
                modelo = str(input('Modelo: ').upper())
                ano = leiaint('Ano de fabricação: ')
                cadastrarVenda(arcVenda, idcliente, nome, cpf, chave, modelo, ano)
                print(f'Nome : {nome} \n CPF: {cpf} \n Modelo: {modelo} Ano: {ano} ')
                situ = leiaint('Confirmar venda - [1] - SIM / [2] - NÃO: ')
                if situ == 1:
                    situ = 'Vendido'
                else:
                    situ = 'Disponivel'
                substituirMoto(chave, modelo, ano, situ)
                print(f'Venda do veículo {chave}-{modelo} para o cliente {idcliente}-{nome} feita com sucesso')
            elif resposta == 3:
                lerArquivoMotoVenda(arcVenda)
                item = leiaint('Digite qual venda deseja alterar: ')
                print('DADOS DO CLIENTE')
                idcliente = leiaint('Id do cliente: ')
                nome = str(input('Nome do Cliente: ').upper())
                cpf = leiaint('CPF: [APENAS NÚMEROS]')
                print('DADOS DO VEÍCULO')
                chave = leiaint('Chave de Identificação: ')
                modelo = str(input('Modelo: ').upper())
                ano = leiaint('Ano de fabricação: ')
                substituirVenda(item, idcliente, nome, cpf, chave, modelo, ano)
            elif resposta == 4:
                lerArquivoMotoVenda(arcVenda)
            elif resposta == 5:
                lerArquivoMotoVenda(arcVenda)
                chave = leiaint('Qual Venda deseja CANCELAR ? ')
                nova_linha = 'CANCELADA; CANCELADA; CANCELADA; CANCELADA; CANCELADA; CANCELADA'
                removerVenda(arcVenda, chave, nova_linha)
                resposta = leiaint('Retornar com mercadoria para o estoque ? [1]SIM / [2]NÃO')
                if resposta == 1:
                    lerArquivoMoto(arcMotos)
                    chave = leiaint('Qual chave deseja alterar ?')
                    modelo = str(input('Modelo: ').upper())
                    ano = leiaint('Ano: ')
                    print('Situação: 1 - Disponivel / 2 - Vendido')
                    while True:
                        situ = leiaint('Opção: ')
                        if situ == 1:
                            situ = 'Disponivel'
                            break
                        elif situ == 2:
                            situ = 'Vendido'
                            break
                    substituirMoto(chave, modelo, ano, situ)
                if resposta ==2:
                    break
            elif resposta == 6:
                break
            else:
                print('Digite uma opção válida!')
    elif resposta == 4:
        cabeçalho('SAINDO DO SISTEMA')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)
    sleep(1)
