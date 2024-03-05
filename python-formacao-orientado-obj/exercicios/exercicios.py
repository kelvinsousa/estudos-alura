'''
Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

nome
artista
duracao
Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..

'''

class Musica:
    nome = ''
    artista = ''
    duracao = int
    

# instanciando a classe (definindo os objetos)


faixa1 = Musica()
faixa1.nome = 'Bohemian Rhapsody'
faixa1.artista = 'Queen'    
faixa1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234


'''
Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
'''
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'
restaurante_praca.nome = 'Praça'

'''
Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
'''
print(restaurante_praca.categoria)

'''
Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
'''

print(f'O restaurante {restaurante_praca.nome} está ativo!') if restaurante_praca.ativo else print(f'O restaurante {restaurante_praca.nome} está inativo!')

'''
Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
'''

categoria = restaurante_praca.categoria
print(categoria)

'''
Altere o valor do atributo nome para 'Bistrô'.
'''

restaurante_praca.nome = 'Bistrô'

print(restaurante_praca.nome)

'''
Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
'''

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(restaurante_pizza.nome, restaurante_pizza.categoria)

'''
Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

'''
print(f'A categoria do {restaurante_pizza.nome} é Fast Food') if restaurante_pizza.categoria == 'Fast Food' else print(f'A categoria do {restaurante_pizza.nome} não é Fast Food')

'''
Mude o estado da instância restaurante_pizza para ativo.
'''

restaurante_pizza.ativo = True


'''
No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

class Musica:
    nome = ''
    artista = ''
    duracao = int
COPIAR CÓDIGO
Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.


'''

class Musica:
    
    musicas = []
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
   
    def listando_musicas():
        i = 0
        for indice, musica in enumerate(Musica.musicas):
            print(f'Faixa {indice + 1}: {musica.nome}, Artista: {musica.artista}, Duração: {musica.duracao}')
    

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

Musica.listando_musicas()