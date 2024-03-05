"""
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""

pessoa = {
    'nome': 'Mariellen',
    'sobrenome': 'Sousa',
    'idade': 29,
    'cidade': 'Americana'    
}


"""
2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""

pessoa.update({'idade': 30})
print(pessoa['idade'])

pessoa['profissao'] = 'Fisioterapeuta'
print(pessoa)

pessoa.pop("cidade")

print(pessoa)

"""
3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
"""

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


"""
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""

if 'sexo' in pessoa:
    print('Existe a chave no dicionário')
else:
    print('Não existe a chave no dicionário')
    
frase = 'No meio da floresta, havia uma pequena cabana. A cabana era feita de madeira e tinha um telhado de palha. Dentro da cabana, morava um velho sábio. O velho sábio era um homem gentil e sábio. Ele passava seus dias ensinando a sabedoria às pessoas que o visitavam.'

contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    
    # Essa linha atualiza o dicionário contagem_palavras com a contagem da palavra atual. Ela usa o método get() para obter o valor atual da palavra no dicionário, ou 0 se a palavra não estiver no dicionário. Em seguida, ela soma 1 a esse valor e atribui o resultado à palavra no dicionário. Por exemplo, se a palavra for "Python", ela verifica se "Python" está no dicionário. Se não estiver, ela usa o valor 0. Se estiver, ela usa o valor que estiver associado a "Python". Depois, ela soma 1 a esse valor e coloca o resultado no dicionário como o novo valor de "Python".

print(contagem_palavras)