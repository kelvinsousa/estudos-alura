
class Cliente:
    def __init__(self, nome):
        self._nome = nome
    
    
    @property
    #com o property não precisamos passar os () do método ao chama-lo.
    def nome(self):
        print(self._nome.title())
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome

cliente = Cliente('kelvin')

cliente.nome
cliente.nome = 'Ellen'
cliente.nome
#Agora, quando digitarmos nos console cliente.nome, sem a adição dos parênteses, e conseguiremos que o método seja executado como antes.