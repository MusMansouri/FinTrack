la librairie `requests` nous sert a envoyer des requete et recevoir des reponses
et 'BeautifulSoup' nous permet de transformer les reponses en données utilisable  
l'inspection find nou permet de trouver ce qu'on cherche dans notre reponse
on ecrit prix_element.text.replace('$','') pour nettoyer notre chaine de caracter
on utilise float() pour convertire notre chaine de caracter en nombre reel
Voici un résumé structuré de tout ce que nous avons vu, formaté pour ton fichier notes.md. Tu peux copier-coller ce contenu directement.Markdown# 🐍 Apprendre la Data Visualization avec Python

## 1. Installation des outils 🛠️
Pour faire des graphiques, Python a besoin d'une librairie externe appelée **Matplotlib**.
Comme elle n'est pas installée par défaut, on utilise `pip` (le gestionnaire de paquets).

**Commande dans le terminal :**
```bash
py -m pip install matplotlib
py : Le lanceur Python.-m : Option pour exécuter un module.pip : Le programme qui installe les librairies.2. Lecture et Nettoyage des Données 🧹Avant de tracer, il faut préparer les données. Les données lues depuis un fichier texte sont toujours du texte (string).Le piège à éviter :Si on ne convertit pas les prix en nombres, Python les trie par ordre alphabétique ("100" arrive avant "9").✅ Solution : Utiliser float() pour convertir le texte en nombre décimal.Structure du code de lecture :Pythondates = []
prix = []

with open('bitcoin_history.txt', 'r') as f:
    for ligne in f:
        morceaux = ligne.split(',')     # Coupe la ligne à la virgule
        dates.append(morceaux[0])       # Ajoute la date (texte)
        prix.append(float(morceaux[1])) # Ajoute le prix (converti en nombre)
3. Tracer le graphique avec Matplotlib 📈Une fois les listes dates et prix prêtes, on utilise le module pyplot (souvent renommé plt).CommandeActionplt.plot(x, y)Prépare la courbe avec les données X et Y.plt.title("...")Ajoute un titre au-dessus du graphique.plt.xlabel("...")Nomme l'axe horizontal (X).plt.ylabel("...")Nomme l'axe vertical (Y).plt.xticks(rotation=45)Pivote les étiquettes de l'axe X (utile pour les dates).plt.show()Indispensable : Affiche la fenêtre du graphique.4. Code Final (visualisation.py) 💻Pythonimport matplotlib.pyplot as plt

dates = []
prix = []

with open('bitcoin_history.txt', 'r') as f:
    for ligne in f:
        morceaux = ligne.split(',')
        dates.append(morceaux[0])
        prix.append(float(morceaux[1]))

# Création du graphique
plt.plot(dates, prix)

# Personnalisation
plt.title("Courbe d'évolution du prix du Bitcoin")
plt.xlabel("Date")
plt.ylabel("Prix ($)")
plt.xticks(rotation=45)

# Affichage
plt.show()