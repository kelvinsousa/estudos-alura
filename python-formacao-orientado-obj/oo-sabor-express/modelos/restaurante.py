



# Criando uma classe:

# class Restaurante:
#     nome= ''
#     categoria = ''
#     ativo = False
    

# # Instanciando a classe

# restaurante_japa = Restaurante()
# restaurante_japa.nome = 'Sushido'
# restaurante_japa.categoria = 'Japonesa'
# restaurante_japa.ativo = False

# # print(dir(restaurante_japa)) # para ver todos os métodos que o objeto possui
# print(vars(restaurante_japa)) # verificando as variáveis que o objeto possui em forma de dict.


'''
Otimizando a classe para que os objetos recebem os mesmos atributos
'''

# class Restaurante:
    
#     # __metodo__ são metodos especiais ou dunder methods
#     def __init__(self, nome, categoria): #metodo construtor
#         self.nome = nome
#         self.categoria = categoria
#         self.ativo = False
        
#     def __str__(self): #  um método especial que define como o objeto da classe será representado em uma string.
#         return f'{self.nome} | {self.categoria} | {self.ativo}'
        

# restaurante_japa = Restaurante('Sushido', 'Japonesa')


# print(restaurante_japa)

from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

'''
criando uma lista de restaurantes para que possamos listar vários restaurantes de uma só vez.
'''

class Restaurante:
    '''Representa um restaurante e suas características.'''
    
    restaurantes = []
    def __init__(self, nome, categoria): # O Self é uma convensão que representa a instância da própria classe
        '''Inicializa uma instância de Restaurante.
        
        Parâmetros
        - nome(str): O nome do restaurante.
        - categoria(str): A categoria do restaurante.
        '''
        self._nome = nome.title() # já podemos setar uma formatação de string aqui
        self._categoria = categoria.title()
        self._ativo = False #quando setamos o atributo com o _ por convensão estamos deixando ele privado, para os devs ter um cuidado para que esse atributo não possa vir a ser alterado pelo user. É sim somente como permissão de 'leitura' da classe.
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        '''Retorna uma representação em string do Restaurante.'''
        
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    
    #criando um método própria dentro da classe, esse método é referente a classe toda e não a um obj específico por isso passamos o @classmethods. Ele não modifica nada, só deixa legível para os devs.
    @classmethod
    def listando_restaurantes(cls): # por convensão utiliza o cls quando é definido o classmethod
        '''Exibe uma lista formatada de todos os restaurantes.'''
        print(f'{"Nome:".ljust(25)} | {"Categoria:".ljust(25)} |{"Avaliacao".ljust(25)} | Status:')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')
    
    #modifica como o atributo é lido.
    @property
    def ativo(self):
        '''Retorna uma representação pt-br para True or False do booleano.'''
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_estado(self):
        '''Altera o estaddo de atividade do restaurante.'''
        self._ativo = not self._ativo
        
    def receber_avaliacao(self):
        '''Registra a avaliação para o restaurante.
        
        Parâmetros
        - nome(str): O nome do cliente que fez a avaliação
        - nota(float): A nota atribuída ao restaurante.
        '''
        cliente = input(f'Avaliação do Restaurante {self._nome}. Qual seu nome? ').title()
        while True:
            nota = float(input('Insira a nota de 0 a 5: '))
            if 0 <= nota <= 5:
                break
            else:
                print('Você digitou uma nota inválida.')          
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''Calcula a média das avaliações dos restaurantes.'''
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        
        media = round(soma_das_notas/quantidade_notas, 1)
        return media

    # def adicionar_bebida_cardapio(self,bebida):
    #     self._cardapio.append(bebida)
        
    # def adicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    def adicionar_no_cardapio(self, item): # o self é os dados do obj que estamos instanciando no caso o restaurante, e o item é o prato/bebida.
        
        if isinstance(item, ItemCardapio): # a funcao isinstance vai ser verdadeira se o item que passamos como argumento for uma instancia da classe itemcardapio ou derivada. Agora nao importa o tipo do item. Agora nao importa o tipo do item, se for um derivado ele adc na lista.
            self._cardapio.append(item)
    
    @property # informa que é só leitura, nao tem manipulação
    def exibir_cardapio(self):
        print(f'Cárdapio do restaurante {self._nome}\n')
        
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${item._preco} | Descrição: {item._descricao}.'
                print(mensagem_prato)
                
            elif hasattr(item, '_tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${item._preco} | Tipo: {item._tipo} | Tamanho: {item._tamanho}.'
                print(mensagem_sobremesa)
            else:
                mensagem = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${item._preco} | Tamanho: {item._tamanho}.'
                print(mensagem)