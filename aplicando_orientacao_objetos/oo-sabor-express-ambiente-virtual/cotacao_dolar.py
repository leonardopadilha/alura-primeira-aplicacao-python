import requests
import json

url = "https://economia.awesomeapi.com.br/last/USD-BRL"

response = requests.get(url)

# if response.status_code == 200:
  # print(response)

if response.status_code == 200:
  dados_json = response.json()
  cotacao = float(dados_json['USDBRL']['bid'])
  mensagem = f"U$ 1 corresponde a R$ {cotacao:.2f}"
  print(mensagem)

