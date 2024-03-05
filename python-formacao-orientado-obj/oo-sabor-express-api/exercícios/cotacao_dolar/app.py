

import requests 

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print()