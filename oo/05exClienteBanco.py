class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, numeroConta):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.numeroConta = numeroConta
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, CPF: {self.cpf}, Número da Conta: {self.numeroConta}"

    @classmethod
    def criar_conta(self, nome, idade, endereco, cpf, numeroConta):
        return (nome, idade, endereco, cpf, numeroConta)

cliente1 = ClienteBanco("João", 30, "Rua A, 123", 1000, "001")
cliente2 = ClienteBanco("Maria", 25, "Rua B, 456", 2000, "002")
cliente3 = ClienteBanco("Pedro", 35, "Rua C, 789", 1500, "003")

print("Informações do Cliente 1:")
print(cliente1)
print("\nInformações do Cliente 2:")
print(cliente2)
print("\nInformações do Cliente 3:")
print(cliente3)