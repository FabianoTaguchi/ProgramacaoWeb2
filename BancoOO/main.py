from modelos.Agencia import Agencia
import os

def main():
    os.system('cls')
    agencia1 = Agencia('Banco do Brasil', 'Rua Dom Pedro', 1670)
    print(agencia1)

if __name__ == '__main__':
   main()
