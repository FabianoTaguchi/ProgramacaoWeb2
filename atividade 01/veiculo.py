import os

veiculos = [{'nome':'Fiat Strada', 'categoria':'Utilitário', 'ativo':False}, 
            {'nome':'VW Amarok', 'categoria':'Caminhonete', 'ativo':True},
            {'nome':'Fiat Argo', 'categoria':'Hatch', 'ativo':False}]

def exibirNomePrograma():
    print('SISTEMA DE FROTAS DE VEÍCULOS 1.0')

def exibirOpcoes():
    print('1. Cadastrar veículo')
    print('2. Listar veículos')
    print('3. Alternar estado de um veículo')
    print('4. Sair\n')

def finalizar():
    exibirSubtitulo('Finalizar app')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarVeiculo():
    exibirSubtitulo('Cadastro de novos veículos')
    nomeVeiculo = input('Digite o nome do veículo a ser cadastrado: ')
    categoria = input(f'Digite a categoria do veículo {nomeVeiculo}: ')
    dadosVeiculo = {'nome':nomeVeiculo, 'categoria':categoria, 'ativo':False}
    veiculos.append(dadosVeiculo)
    print(f'O veículo {nomeVeiculo} foi cadastrado com sucesso!')
    voltarMenuPrincipal()

def listarVeiculo():
    exibirSubtitulo('Listagem de veículos')
    print(f'{'Nome do veículo'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for veiculo in veiculos:
        nomeVeiculo = veiculo['nome']
        categoria = veiculo['categoria']
        ativo = 'ativado' if veiculo['ativo'] else 'desativado'
        print(f'- {nomeVeiculo.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltarMenuPrincipal()

def alterarVeiculo():
    exibirSubtitulo('Alterar estado do veículo')
    nomeVeiculo = input('Digite o nome do veículo que deseja alterar o status: ')
    veiculoEncontrado = False

    for veiculo in veiculos:
        if nomeVeiculo == veiculo['nome']:
            veiculoEncontrado = True
            veiculo['ativo'] = not veiculo['ativo']
            mensagem = f'O veiculo {nomeVeiculo} foi ativado com sucesso' if veiculo['ativo'] else f'O veiculo {nomeVeiculo} foi desativado com sucesso'
            print(mensagem)
            
    if not veiculoEncontrado:
        print('O veiculo não foi encontrado')
            
    voltarMenuPrincipal()

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            cadastrarVeiculo()
        elif opcaoEscolhida == 2: 
            listarVeiculo()
        elif opcaoEscolhida == 3: 
            alterarVeiculo()
        elif opcaoEscolhida == 4: 
            finalizar()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()