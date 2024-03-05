'''
Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

'''

from livro import Livro


livro1 = Livro('Harry Potter e a Pedra Filosofal', 'JK Rowling', 1996)
Livro.emprestar(livro1)
Livro.disponivel(livro1)


print(f'Livros disponíveis para locação: {Livro.verificar_disponibilidade(2019)}')
