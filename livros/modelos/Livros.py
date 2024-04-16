from modelos.Biblioteca import Biblioteca

class Livro:
    livros = []

    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.anoPublicacao}"

    def emprestar(self, aluno, data):
        emprestimo = Biblioteca(aluno, data)
        self.disponivel = False

    @staticmethod
    def verificarDisponibilidade(ano):
        livrosDisponiveis = []
        for livro in Livro.livros:
            if livro.anoPublicacao == ano and livro.disponivel:
                livrosDisponiveis.append(livro)
        return livrosDisponiveis


