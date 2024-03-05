'''
Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
'''
from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo
    
    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Ligado: {status} | Tipo: {self._tipo}.'
    
