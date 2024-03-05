from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #passando a classe dentro dos () de uma outra classe ela herda todos os atributos, métodos etc.
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
        #super é um objeto especial que permite que acesse informações de outra classe.
        
    def __str__(self) -> str:
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        