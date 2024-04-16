numeros = []

for numero in range(10):
    itemDigitado = int(input('Digite um valor: ') )
    if(itemDigitado % 2 ==0):
        itemDigitado=itemDigitado+100
    numeros.append(itemDigitado)

for numero in numeros:
    print(numero)