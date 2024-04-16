
while True:
    print('Selecione uma das opções abaixo: ')
    print('1 - Olá mundo ')
    print('2 - Programação em Python ')
    print('3 - Modularização em Python ')
    opcao = int(input('Selecione a opção: '))
    
    if opcao == 1:
        print('Olá mundo!')
    elif opcao == 2:
        print('Programação em Python!')
    elif opcao == 3:
        print('Modularização em Python')
    else:
        print('Opção inválida')

    opcao = input('Para escolher uma opção novamente tecle S: ')
    if opcao.lower() != 's':
        print('Você pediu para encerrar o programa')
        break 

print('Programa encerrado')
    