import requests
from bs4 import BeautifulSoup

# Nouvelle cible : CoinMarketCap (Bitcoin)
url = "https://coinmarketcap.com/currencies/bitcoin/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(f"Statut de la réponse : {response.status_code}")