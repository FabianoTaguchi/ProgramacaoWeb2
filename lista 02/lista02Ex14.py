listaCompras = [
    {'descrição': 'Água', 'preço': 1.99},
    {'descrição': 'Leite', 'preço': 4.99},
    {'descrição': 'Carne', 'preço': 39.99},
    {'descrição': 'Pizza', 'preço': 79.99},
    {'descrição': 'Chocolate', 'preço': 7.50},
]

barato = None
caro = None
indice = 0

while indice < len(listaCompras):
    item = listaCompras[indice]
    if indice == 0:
        caro = item
        barato = item
    else:
        if item['preço'] > caro['preço']:
            caro = item

        if item['preço'] < barato['preço']:
            barato = item
    indice = indice + 1

print('Produto mais caro: ', caro['descrição'], 'por', caro['preço'],'reais')
print('Produto mais barato: ', barato['descrição'], 'por', barato['preço'],'reais')