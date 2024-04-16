nomes = []

for nome in range(5):
    nome = input('Digite um nome: ')
    nomes.append(nome)

print(nomes)

excluir = int(input('Escolha uma posição entre 0 e 4: '))
if excluir < 0 or excluir > 4:
    print('Limite da lista inválido')
else:
    del nomes[excluir]

print('Lista atualizada')
print(nomes)
