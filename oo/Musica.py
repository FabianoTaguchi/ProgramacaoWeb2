class Musica:
    nome = ''
    artista = ''
    duracao = int


musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
print(f'Música: {musica2.nome} - Banda: {musica2.artista} - {musica2.duracao} segundos')
print(f'Música: {musica3.nome} - Banda: {musica3.artista} - {musica3.duracao} segundos')
