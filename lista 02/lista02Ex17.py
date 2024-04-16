def somar(n1, n2):
    return n1+n2

def multiplicar(n1, n2):
    return n1*n2

def subtrair(n1,n2):
    return n1-n2

def dividir(n1,n2):
    return n1/n2

resultado = 0.0
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print('1 para somar')
print('2 para multiplicar')
print('3 para subtrair')
print('4 para dividir')
opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1: 
        resultado = somar(numero1, numero2)
    case 2: resultado = multiplicar(numero1, numero2)
    case 3: resultado = subtrair(numero1, numero2)
    case 4: resultado = dividir(numero1, numero2)
    case _: print('Opção inválida!')

print(resultado)
