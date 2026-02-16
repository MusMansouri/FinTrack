import pandas as pd  # On renomme toujours pandas en 'pd' par convention
import matplotlib.pyplot as plt
# On crée des données (comme un dictionnaire)
data = {
    "Cryptomonnaie": ["Bitcoin", "Ethereum", "Dogecoin"],
    "Prix": [50000, 3000, 0.20],
    "Variation": ["+5%", "-2%", "+10%"]
}

#  Tableau (DataFrame)
tableau = pd.DataFrame(data)

print("--- Mon Premier DataFrame ---")
print(tableau)

# facile d'avoir des stats :
print("\n--- Statistiques automatiques ---")
print(tableau.describe())
tableau.plot(x='Cryptomonnaie',y='Prix',title='test')
plt.show()
