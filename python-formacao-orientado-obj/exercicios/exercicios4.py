'''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Adicione uma propriedade chamada titular à classe ContaBancaria utilizando a função property. Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.

'''
# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    
    def __init__(self, titular ='', saldo=0, ativo=False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo
    
    # 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.    
    def __str__(self):
        return(f'Titular: {self._titular.ljust(10)} | Saldo: {self._saldo}| Ativo: {self.ativo}')
    
    # def ativar_conta(self):
    #     self._ativo = not self._ativo
    
    # 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return 'Conta ativa' if self._ativo else 'Conta inativa'

        
conta1 = ContaBancaria('Kelvin', 1000)
conta2 = ContaBancaria('Oliver', 79000)
conta3 = ContaBancaria("Carlos", 200)


print('Ativando as contas: ')

print(f"Antes de ativar: Conta ativa? {conta3.ativo}")

ContaBancaria.ativar_conta(conta3)

print(f"Depois de ativar: Conta ativa? {conta3.ativo}")

# 5) Adicione uma propriedade chamada `titular` à classe ContaBancaria utilizando a função `property`. Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")


# 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    
    clientes = []
    def __init__(self, nome ='', sexo='', idade=0, tempo_cliente=0, tipo_conta='', saldo_inicial=0):
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._tempo_cliente = tempo_cliente
        self._tipo_conta = tipo_conta
        self._saldo_inicial = saldo_inicial
        ClienteBanco.clientes.append(self)
    
    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f'Nome: {cliente._nome} | Sexo: {cliente._sexo} | Idade: {cliente._idade} | Tempo como cliente(anos): {cliente._tempo_cliente} | Tipo CC {cliente._tipo_conta} | Saldo inicial: {cliente._saldo_inicial}')
    
    @classmethod
    def adc_saldo_inicial(cls, titular, saldo_inicial):
        conta =  ContaBancaria(titular, saldo_inicial)
        return conta
    
cliente1 = ClienteBanco('Kelvin', 'M', 30, 7, 'Premium')
cliente2 = ClienteBanco('Oliver', 'M', 25, 10, 'Super Premium')
cliente3 = ClienteBanco('Alfred', 'M', 25, 5, 'Básica')

ClienteBanco.listar_clientes()

conta_cliente1 = ClienteBanco.adc_saldo_inicial("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")