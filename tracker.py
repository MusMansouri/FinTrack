import requests ,datetime ,time
from bs4 import BeautifulSoup



# Nouvelle cible : CoinMarketCap (Bitcoin)
url = "https://coinmarketcap.com/currencies/bitcoin/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

print(f"Statut de la réponse : {response.status_code}")
print(f'{datetime.datetime.now()}')

# ... (le début avec les imports et headers reste pareil)
while True:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # On crée la "soupe"
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Juste pour vérifier, on affiche le titre de la page
        # On cherche la balise <span> qui a exactement cette classe
        # (Copie-colle la classe que tu as trouvée si elle diffère légèrement)
        prix_element = soup.find('span', class_='sc-c1554bc0-0 RbQXx base-text')

        # On vérifie si on a trouvé quelque chose avant d'afficher
        if prix_element:
            # On nettoie le texte
            prix_str = prix_element.text.replace('$', '').replace(',', '')
            
            # On convertit en nombre décimal
            prix_nbr = float(prix_str)
            
            print(f"Le prix actuel est : {prix_nbr}")
            print(f"Si j'achète 2 Bitcoins, cela me coûtera : {prix_nbr * 2}")
        else:
            print("Mince, le prix est introuvable avec cette classe.")

    with open('bitcoin_history.txt','a') as f: 
        f.write(f'{datetime.datetime.now()},{prix_str}\n')
    time.sleep(60)