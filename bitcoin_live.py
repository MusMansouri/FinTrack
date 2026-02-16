import requests , time

# import requests # On importe le "téléphone" pour appeler l'API

# # L'adresse du "serveur" (L'URL de l'API)
# # On demande : "simple/price", pour l'id "bitcoin", en monnaie "usd"
# url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# print("Appel de l'API en cours...")

# # On lance l'appel (GET = "Obtenir")
# reponse = requests.get(url)

# # On affiche le résultat brut (le texte que le serveur nous renvoie)
# print(reponse.text)

# url='https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
# while True:
    
#     response = requests.get(url)

#     # Étape 1 : Convertir la réponse (texte) en vrai Dictionnaire Python
#     data = response.json()

#     # Étape 2 : Aller chercher l'info (Navigation dans les clés)
#     # On rentre dans 'bitcoin', puis dans 'usd'
#     prix_actuel = data['bitcoin']['usd']
    
#     print(f"Le Bitcoin vaut actuellement : {prix_actuel} $")


cryptos=['bitcoin','dogecoin']

def obtenir_prix(i):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={cryptos[i-1]}&vs_currencies=usd" 
    reponse = requests.get(url)
    data=reponse.json()
    prix_actuel = data[f'{cryptos[i-1]}']['usd']
    
    print(f"\n -----------Le {cryptos[i-1]} vaut actuellement : {prix_actuel} $-------------\n")
    

 
print('\n------Bonjour dans ma petite app\API-------\n ')
while True:
    
    print('\n---MENU---')
    print('\n1. Connaitre le prix du bitcoin actuel')
    print('\n2. Connaitre le prix de dogecoin actuel')
    print('\n3.Quiter')
    repmenu=int(input('\nEntrer une reponse '))

    if repmenu == 1:
        obtenir_prix(1)
    elif repmenu==2:
        obtenir_prix(2)

    elif repmenu==3:
        break
    else: 
        print('\nReponse introuvable dans le menu ')
    
