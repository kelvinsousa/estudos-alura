'''
Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
'''

from livro import Livro

livro1 = Livro('Harry Potter e a Pedra Filosofal', 'JK Rowling', 1996)
livro2 = Livro('O poder da mente', 'Erik Hotz', 2019)

print(livro1)
print(livro2)