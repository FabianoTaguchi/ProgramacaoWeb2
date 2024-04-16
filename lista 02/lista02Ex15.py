pessoas = [
    {'nome': 'Joãozinho', 'sobrenome': 'da Silva' },
    {'NOME': 'Mariazinha', 'sobrenome': 'de Souza' }, 
    {'nome': 'Gabriel', 'sobrenome': 'Schade' },
    {'NOME': 'Joana', 'sobrenome': 'da Silva' },
    {'nome': 'Everton', 'sobrenome': 'Schmit' },
]

print(type(pessoas))
for pessoa in pessoas:
    nome = pessoa.get('nome', None)
    sobrenome = pessoa.get('sobrenome', None)
    print(nome, sobrenome)