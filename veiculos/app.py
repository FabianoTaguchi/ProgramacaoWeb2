from modelos.Veiculo import Veiculo

veiculo1 = Veiculo('S-10', 'Caminhonete')
veiculo2 = Veiculo('Argo', 'Hacth')
veiculo3 = Veiculo('Kombi','Utilitário')

veiculo1.receberAvaliacao('Teste', 7)
veiculo1.receberAvaliacao('Teste', 11)
veiculo3.receberAvaliacao('Teste', 10)

def main():
    Veiculo.listarVeiculos()

if __name__ == '__main__':
    main()