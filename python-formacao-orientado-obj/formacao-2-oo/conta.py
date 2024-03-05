
class ContaCorrente:
    def __init__(self, banco, agencia, conta_corrente, titular, saldo, limite = 5000.0):
        self._banco = banco
        self._agencia = agencia
        self._conta_corrente = conta_corrente
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._codigo_banco
        
    def __str__(self):
        return f'Banco {self._banco} | Ag: {self._agencia} | CC: {self._conta_corrente} | Titular {self._titular} | Saldo: {self._saldo} | Limite: {self._limite}'
    
    def extrato(self):
        print(f'O saldo para a conta é do {self._titular} é de R${self._saldo}.')
    
    #deixando o método privado, para ser usado dentro da classe e não no terminal
    def _pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self._saldo + self._limite)
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def sacar(self, valor):
        if self._pode_sacar(valor):
            self._saldo -= valor
            print(f'Saque de R${valor} realizado na conta {self._agencia}-{self._conta_corrente}')
        else:
            print(f'Saldo insuficiente R${self._saldo + self._limite} para o saque de R${valor}')
            
    def depositar(self, valor):
        self._saldo += valor
        print(f'Depósito de R${valor} realizado na conta {self._agencia}-{self._conta_corrente}')
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    

    
        
    
    '''
    Sempre que precisarmos acessar um atributo privado do obj criamos um novo método para isso. #GET
    
    def get_saldo(self):
        return self._saldo 
    
    def get_limite(self):
        return self._limite
    
    def get_titular(self):
        return self._titular
    '''
        
    
    #Refatorando o #GET (GETTER) criado, adicionando a property
    @property
    def saldo(self):
        return print(self._saldo)
    @property
    def limite(self):
        return print(self._limite)
    @property
    def titular(self):
        return print(self._titular)
    
    ''' 
    Sempre que precisarmos alterar um atributo privado do obj criamos um novo método para isso. #SET
    
    def set_limite(self, limite):
        self._limite = limite 
    '''
        
    #Refatorando os #SET (SETTER)
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        
    
    @staticmethod
    def codigo_banco():
        return '001'
                
    # Só criar os métodos get e set quando realmente fizer sentido.

# conta1 = ContaCorrente('Bradesco', '0215', '02382628', 'Kelvin Sousa', 3450.0)
# conta2 = ContaCorrente('Bradesco', '0215', '02382699', 'Ellen Sousa', 450.0)

# conta1.extrato()
# conta1.depositar(1000)
# conta1.transferir(2000, conta2)
# conta1.extrato()
# conta2.extrato()
# # print(conta1.get_saldo())
# # print(conta1.get_limite())
# # conta1.set_limite(10000.0)
# # print(conta1.get_limite())
# conta1.saldo
# conta1.limite
# conta1.limite = 10000.0
# conta1.limite
# conta1.sacar(200000)

print(ContaCorrente.codigo_banco()) #Não depende de um objeto para retornar o valor, já que ele é um método da classe @staticmethod