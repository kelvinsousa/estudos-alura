'''
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 

Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 

Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 

Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

'''

class Pessoa:
    
    pessoas = []
    def __init__(self, nome ='', idade =0, profissao =''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        Pessoa.pessoas.append(self)
    
    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade} | Profissão: {self._profissao}'
    
    
    @classmethod
    def listando_pessoas(cls):
        print(f'{"Nome:".ljust(15)} | Idade: | Profissão')
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome.ljust(15)} |     {pessoa._idade} | {pessoa._profissao}')
    
    def aniversario(self):
        self._idade += 1
    
    @property
    def saudacao(self):
        print(f'Olá, sou {self._nome} e trabalho com {self._profissao}') if self._profissao else print(f'Olá, sou {self._nome}')
        
        
# Criando 3 instâncias da classe Pessoa
pessoa_1 = Pessoa('Kelvin', 30, 'Analista')
pessoa_2 = Pessoa('Ellen', 30, 'Fisioterapeuta')
pessoa_3 = Pessoa('Alfred', 22, 'Vasf')
pessoa_4 = Pessoa('Oliver', 22, 'Herdeiro')

# Imprimindo informações iniciais
print("Informações Iniciais:")
Pessoa.listando_pessoas()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
pessoa_1.aniversario()
pessoa_3.aniversario()

Pessoa.listando_pessoas()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
pessoa_1.saudacao
pessoa_2.saudacao
pessoa_3.saudacao
