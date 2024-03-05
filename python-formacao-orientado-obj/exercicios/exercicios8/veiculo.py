'''
Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
'''

from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    
    def __str__(self):
        self._modelo
    
    @abstractmethod
    def ligar(self):
        pass
    
    