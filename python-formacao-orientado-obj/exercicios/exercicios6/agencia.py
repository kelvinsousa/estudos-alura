from banco import Banco

class Agencia(Banco):
    
    def __init__(self, nome, cidade, agencia):
        super().__init__(nome, cidade)
        self._agencia = agencia
        
    def __str__(self):
        return f'Banco: {self._nome}, Cidade: {self._cidade}, Agencia: {self._agencia}'