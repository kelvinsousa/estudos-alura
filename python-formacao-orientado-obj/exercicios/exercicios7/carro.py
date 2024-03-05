'''
Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
'''

from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, modelo, marca, portas):
        super().__init__(modelo, marca)
        self._portas = portas
    # Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
    
    def __str__(self):
        status = 'Ligado' if self._ligado else 'Desligado'
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Ligado: {status} | Portas: {self._portas}'
    