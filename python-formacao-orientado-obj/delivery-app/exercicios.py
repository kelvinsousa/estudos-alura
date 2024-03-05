"""
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_dois = [20, 40, 'a']
lista_valores = []
nomes = ['Mariellen', 'Kelvin', 'Alfredoca', 'Livota']
anos = [1993, 2023]



def main():
    print(numeros)
    resultado_soma_impares = soma_impares(numeros)
    numeros_desc = sorted(numeros, reverse=True)

    print(f'O valor dos números ímpares é {resultado_soma_impares}\n')
    print(f'Os valores ordenados de forma decrescente ficam: {numeros_desc}\n')
    num = int(input('Digite um número para exibir sua tabuada até de 1 a 10: '))
    tabuada(num, numeros)
    print()
    soma_valores = soma(numeros_dois)
    print(soma_valores)
    print()
    soma_valores_tratado(lista_valores)

def soma_impares(numeros):
    soma_impares = 0
    for n in numeros:
        if n % 2 != 0:
            soma_impares += n
        else:
            pass        
    
    return soma_impares


def tabuada(num, numeros):
    print('\n##### Tabuada #####')
    for n in numeros:
        resultado = num * n
        print(f'{num} x {n} = {resultado}')
    
def soma(numeros_dois):
    soma = 0 
    for n in numeros_dois:
        try:
            soma += n
        except TypeError as e:
            print(f'O valor "{n}" não é um número válido e não foi contabilizado na soma!')
    return soma

def soma_valores_tratado(lista_valores):
    soma_valores = 0
    try:
        for valor in lista_valores:
            soma_valores += valor
        media = soma_valores / len(lista_valores)
        print(f"Média dos valores: {media}")
    except ZeroDivisionError:
        print("A lista está vazia, não é possível calcular a média.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
if __name__ == '__main__':
    main()
