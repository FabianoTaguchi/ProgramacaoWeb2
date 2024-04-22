class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrarInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco}")
        print(f"Quantidade: {self.quantidade}")

    def mostrarValorTotalEstoque(self):
        valorTotal = self.preco * self.quantidade
        print(f"O valor total de estoque deste produto é R${round(valorTotal, 2)}")

p2 = Produto("Refrigerante", 4.99, 25)





