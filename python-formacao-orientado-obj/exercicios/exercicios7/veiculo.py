
'''
Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
'''

class Veiculo:
    
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    # Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    
    @property
    def status(self):
        'Ligado' if self._ligado else 'Desligado' #podemos colocar diretamente dentro do método especial __str__ como vamos fazer nas classes filhas.
    
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Ligado: {self.status}.'
       
        
