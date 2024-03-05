
class Banco:
    def __init__(self, nome, cidade):
        self._nome = nome
        self._cidade = cidade
    
    def __str__(self):
        return f'Banco: {self._nome}, Cidade: {self._cidade}'