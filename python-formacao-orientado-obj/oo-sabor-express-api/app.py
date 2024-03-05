import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #endpoint


response = requests.get(url) # get é um verbo do http aonde vamos solicitar um recurso.

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
            
else:
    print(f'O erro foi {response.status_code}')
    
    
# print(dados_restaurante['McDonald’s'])

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
else:
    print(f'O erro foi {response.status_code}')
    
