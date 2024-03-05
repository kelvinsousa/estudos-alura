from fastapi import FastAPI, Query
import requests


app = FastAPI() #aqui estamos armazenando o objeto do FastAPI dentro da variável app

#existem decorators específico do fastapi, nesse caso vamos usar o get.
#@app.get(caminho do endpoint)

@app.get('/api/hello')

def hello_word():
    '''
    Endpoint que exibe uma msg incrível do mundo da programação.
    '''
    return {'Hello': 'World'}


@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para visualizar os cardápios dos restaurantes.
    '''
        
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' #endpoint


    response = requests.get(url) # get é um verbo do http aonde vamos solicitar um recurso.

    if response.status_code == 200:
        dados_json = response.json()
        
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        
        return{'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    
    else:
        return{'Erro':f'{response.status_code} - {response.text}'}
  
# Criar um servidor para nossa api, no terminal: uvicorn main:app --reload  
# Para acessar a documentação da nossa api acessamos o endpoint /docs do fastapi
# listando todo o cardápio: http://127.0.0.1:8000/api/restaurantes
# usando a query para buscar um restaurante: http://127.0.0.1:8000/api/restaurantes/?company=KFC
# acessando a documentação: http://127.0.0.1:8000/docs