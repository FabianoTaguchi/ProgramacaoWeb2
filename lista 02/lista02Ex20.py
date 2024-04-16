import os

def solicitar():
    numeros = []
    for i in range(3):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    return numeros

def maior(numeros):
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    return maior


def finalizar():
    os.system('cls')

def main():
    finalizar()
    numeros = solicitar()
    maiorNumero = maior(numeros)
    print('O maior número digitado foi ', maiorNumero)    

if __name__ == '__main__':
    main()


