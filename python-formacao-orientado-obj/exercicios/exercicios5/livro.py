

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
    
    # Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
    def __str__(self):
        return f'O livro {self._titulo} pertence ao autor(a) {self._autor} e teve sua publicação no ano de {self._ano_publicacao}.'
    
    def emprestar(self):
        self._disponivel = False

    @classmethod
    def disponivel(cls, livro):
        print(f'O livro {livro._titulo} está disponível') if livro._disponivel else print(f'O livro {livro._titulo} não está disponível')
        
    @staticmethod
    def verificar_disponibilidade(ano):
        # livros_disponiveis = []
        # for livro in Livro.livros:
        #     if livro._ano_publicacao == ano and livro._disponivel:
        #         livros_disponiveis.append(livro._titulo)        
        livros_disponiveis = [livro._titulo for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

# Crie duas instâncias da classe Livro e imprima essas instâncias.

livro1 = Livro('Harry Potter e a Pedra Filosofal', 'JK Rowling', 1996)
livro2 = Livro('O poder da mente', 'Erik Hotz', 2019)
livro3 = Livro('Mindset', 'Tobias Jacob', 2019)
livro4 = Livro('Borboletas', 'Alfred Frederick', 2019)


# Livro.disponivel(livro1)
# print('Emprestou o livro')
# livro1.emprestar()
# Livro.disponivel(livro1)

# 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

livros_disp = Livro.verificar_disponibilidade(2019)
# print()