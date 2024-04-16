listaCompras = [
    {'descrição': 'Água', 'preço': 1.99},
    {'descrição': 'Leite', 'preço': 4.99},
    {'descrição': 'Carne', 'preço': 39.99},
    {'descrição': 'Pizza', 'preço': 79.99},
    {'descrição': 'Chocolate', 'preço': 7.50},
]

for produto in listaCompras:
    print('Produto:', produto['descrição'], 'por', (produto['preço']), 'reais.')