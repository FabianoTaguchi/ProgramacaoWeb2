class Pessoa:
   def __init__(self, nome):
      self.nome = nome
 
   def __str__(self):
      return f'Nome: {self.nome}'

class Professor(Pessoa):
   def __init__(self, nome, titulacao):
      super().__init__(nome)
      self.titulacao = titulacao
 
   def __str__(self):
      return 'Nome:'+self.nome+' Titulação:'+self.titulacao

pessoa = Pessoa('Maria')
professor = Professor('Roque', 'Doutor')
print(pessoa)
print(professor)