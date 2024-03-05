'''
Exercícios
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

'''


class Carros:
    
    def __init__(self, fabricante, modelo, cor, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
peugeot_408 = Carros('Peugeot', '408', 'Prata', 2012)

print(peugeot_408.modelo)

'''
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

'''
class Restaurante:
    
    def __init__(self, nome, categoria, ifood, delivery, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ifood = ifood
        self.delivery = delivery
        self.ativo = ativo
    
    
    '''
    Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    '''
    def __str__(self):
        return f'Nome: {self.nome} | Cat: {self.categoria} | Cadastrado iFood: {self.ifood} | Faz delivery: {self.delivery} | Ativo: {self.ativo}'

restaurante_1 = Restaurante('Sushido', 'Japonesa', True, False, True)

print(restaurante_1)



'''
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
'''

class Cliente:
    
    clientes = []
    
    def __init__(self, nome,sexo, uf, primeira_compra, ativo):
        self.nome = nome
        self.sexo = sexo
        self.uf = uf
        self.primeira_compra = primeira_compra
        self.ativo = ativo
        Cliente.clientes.append(self)
    
    def listando_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome = {cliente.nome} | Sexo = {cliente.sexo} | UF = {cliente.uf} | Ativo = {cliente.ativo}')


cliente_1 = Cliente('Kelvin', 'Masculino', 'SP', True, True)
cliente_2 = Cliente('Alfred', 'Masculino', 'MG', False, True)
cliente_3 = Cliente('Oliver', 'Masculino', 'RJ', False, False)


Cliente.listando_clientes()