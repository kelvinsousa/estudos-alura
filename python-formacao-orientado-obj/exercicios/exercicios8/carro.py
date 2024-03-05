'''
Crie uma nova classe chamada Carro que herda da classe Veiculo.
No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
'''
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor
    
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Cor: {self._cor}'
    
    def ligar(self):
        print(f"O carro {self._modelo} está ligado.")