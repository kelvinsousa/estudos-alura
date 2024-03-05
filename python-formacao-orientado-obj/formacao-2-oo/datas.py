class Data:
    def __init__(self, d,m,a):
        self.dia = d
        self.mes = m 
        self.ano = a 
    
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    

data1 = Data(19,10,1993)

print(data1)