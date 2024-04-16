class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.ano}'
    
    def listarCarros():
        for novoCarro in Carro.carros:
            print(f'{novoCarro.modelo} ano {novoCarro.ano}')

carro1 = Carro('Fusca', 'Azul', 1970)
carro2 = Carro('Gol', 'Preto', 2020)
carro3 = Carro('Palio', 'Vermelho', 2016)
carro4 = Carro('S-10', 'Prata', 2019)
carro5 = Carro('Celta', 'Branco', 2010)

Carro.listarCarros()

