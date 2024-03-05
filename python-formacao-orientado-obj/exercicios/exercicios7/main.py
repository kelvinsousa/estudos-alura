
'''
Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
'''


from carro import Carro
from moto import Moto

def main():
    
    # Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
    
    peugeot_408 = Carro('Peugeot', '408', portas=4)
    citroen_c3 = Carro('Citroen', 'C3', portas=4)
    meriva = Carro('Chevrolet', 'Meriva', portas=4)
    
    susuki = Moto('Susuki', 'S900', 'Esportiva')
    kawasaki = Moto('Kawasaki', 'k1100', 'Esportiva')
    titan = Moto('Honda', 'Titan 125', 'Passeio')

    # Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

    print(peugeot_408)
    print(citroen_c3)
    print(meriva)
    print(susuki)
    print(kawasaki)
    print(titan)



if __name__ == '__main__':
    main()