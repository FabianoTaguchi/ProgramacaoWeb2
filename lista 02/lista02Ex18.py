import os

def solicitar():
    numeros = []
    for i in range(4):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    return numeros

def maior(numeros):
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    return maior

def dobrar(numero):
    return numero * 2

def finalizar():
    os.system('cls')

def main():
    finalizar()
    numeros = solicitar()
    maiorNumero = maior(numeros)
    dobrarNumero = dobrar(maiorNumero)
    print(f"O dobro do maior número ({maiorNumero}) é: {dobrarNumero}")       

if __name__ == '__main__':
    main()


