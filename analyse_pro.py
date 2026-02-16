import pandas as pd
import matplotlib.pyplot as plt
# Chargement ultra-rapide
# header=None : On dit à Python qu'il n'y a pas de titre dans le fichier texte
# names=[...] : On donne nous-mêmes les noms aux colonnes
df = pd.read_csv("bitcoin_history.txt", header=None, names=["Date", "Prix"])

# Affiche les 5 premières lignes pour vérifier
print("--- Aperçu des données ---")
print(df.head())

# Vérifie les types de données (Est-ce que le Prix est bien un nombre ?)
print("\n--- Infos techniques ---")
print(df.info())
# ... (après le chargement du fichier)

print("\n--- Statistiques Complètes ---")
print(df.describe())

print("\n--- Jours où le Bitcoin a explosé (> 55 000) ---")

# La syntaxe magique : df [ condition ]
boom = df[df['Prix'] > 55000]

print(boom)
print("\n--- Record Historique (Top 5) ---")
# On trie par 'Prix', en ordre décroissant (ascending=False)
top5 = df.sort_values(by='Prix', ascending=False).head()
print(top5)
df.plot(x='Date', y='Prix', title='Prix du Bitcoin')
plt.xticks(rotation=45)
plt.show()
# On prend notre variable 'top5' et on l'écrit dans un fichier
# index=False : pour ne pas écrire les numéros de ligne (0, 1, 2...) dans le fichier
top5.to_csv("top5_records.csv", index=False)
print("Fichier 'top5_records.csv' généré avec succès !")
df.to_csv('bitcoin_history.csv') 
print("Fichier 'bitcoin_history.csv' généré avec succès !")