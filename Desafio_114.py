import urllib.request
from wsgiref import headers

url = 'https://www.pudim.com.br'
cabeçalho = {"User-Agent": "Mozilla/5.0"}
requisição = urllib.request.Request(url, headers=cabeçalho)
try:
    urllib.request.urlopen(requisição)
except Exception as erro:
    print(f"Infelizmente tivemos o erro: {erro.__class__}")
else:
    print("O site está acessível no momento.")
