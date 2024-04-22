from Produto import Produto

class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, quantidade, dataValidade):
        super().__init__(nome, preco, quantidade)
        self.dataValidade = dataValidade

    def mostrarValidade(self):
        print(f"O produto vence no dia {self.dataValidade}")
    
    def mostrarInfo(self):
        super().mostrarInfo()
        print("="*30)
        print(f"Esse produto é perecível!")
        print("="*30)

p3 = ProdutoPerecivel('Leite', 7.99, 10, '10/05/2023')
p3.mostrarInfo()
p3.mostrarValorTotalEstoque()
p3.mostrarValidade()



