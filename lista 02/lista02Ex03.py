import os
os.system('cls')

numeros = [1,3,6,10,5,23]
numeroDigitado = int(input('Digite um número: '))

if numeroDigitado in numeros:
    print(f'O número {numeroDigitado} está na lista')
else:
    print(f'O número {numeroDigitado} não está na lista')