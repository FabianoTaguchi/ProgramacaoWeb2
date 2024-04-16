import os

def solicitar():
    return input('Digite um nome: ')

def adicionar(lista, nome):
    lista.append(nome)

def escrever(lista):
    for nome in lista:
        print(nome)

def pesquisar(nomes):
    nome = input('Digite o nome que deseja pesquisar: ')
    if nome in nomes:
        print(f"O nome '{nome}' foi encontrado na lista.")
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")

def finalizar():
    os.system('cls')

def main():
    finalizar()
    nomes = []
    for contador in range(0,5):
        nome = solicitar()
        adicionar(nomes, nome)
    
    print('1 para pesquisar')
    print('2 para imprimir nomes')
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1: resultado = pesquisar(nomes)
        case 2: resultado = escrever(nomes)
        case _: print('Opção inválida!')  

if __name__ == '__main__':
    main()


