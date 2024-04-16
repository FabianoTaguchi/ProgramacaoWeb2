from modelos.Avaliacao import Avaliacao

class Veiculo:
    veiculos = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Veiculo.veiculos.append(self)
    
    def __str__(self):
        return f'{self._nome} - {self._categoria}'
    
    @classmethod
    def listarVeiculos(self):
        print(f'{'Nome do veículo'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for veiculo in self.veiculos:
            print(f'{veiculo._nome.ljust(25)} | {veiculo._categoria.ljust(25)} | {str(veiculo.mediaAvaliacoes).ljust(25)} |{veiculo.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternarEstado(self):
        self._ativo = not self._ativo

    def receberAvaliacao(self, cliente, nota):
        if 0 < nota <= 10: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def mediaAvaliacoes(self):
        if not self._avaliacao:
            return '-'
        somaNotas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidadeNotas = len(self._avaliacao)
        media = round(somaNotas / quantidadeNotas, 1)
        return media