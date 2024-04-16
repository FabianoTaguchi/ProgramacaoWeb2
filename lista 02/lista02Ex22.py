import os

def solicitar():
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    return numeros

def soma(numeros):
    return sum(numeros)

def media(numeros, soma):
    return soma / len(numeros)

def finalizar():
    os.system('cls')

def main():
    finalizar()
    numeros = solicitar()
    somaFinal = soma(numeros)
    mediaFinal = media(numeros, somaFinal)
    
    print(somaFinal)
    print(mediaFinal)   

if __name__ == '__main__':
    main()


