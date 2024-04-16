from modelos.Livros import Livro  

def main():
    livro1 = Livro('Python é bom', 'Mark Joe', 2022)
    livro2 = Livro('A ciência da informação', 'Emily Klein', 2020)
    livro3 = Livro('Titanic', 'Autor desconhecido', 2020)
    livro4 = Livro('A volta dos que não foram', 'Autor desconhecido', 2020)
    livro5 = Livro('O retorno', 'Paulo José da Silva', 2020)

    livro1.emprestar('Teste', '10/04/2024')
    livro3.emprestar('Fabiano','10/04/2024')
        
    anoDesejado = 2020
    livrosDisponiveis = Livro.verificarDisponibilidade(anoDesejado)

    print(f"Livros disponíveis em {anoDesejado}:")
    for livro in livrosDisponiveis:
        print(livro)

if __name__ == '__main__':
    main()