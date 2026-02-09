# 🐍 Apprendre le Scraping avec Python

## 1. Les Outils (Librairies)

- **requests** : C'est notre "navigateur" ou "facteur". Elle sert à envoyer une demande au site web et à recevoir le code HTML en réponse.
- **BeautifulSoup** (de `bs4`) : C'est notre "traducteur". Elle transforme le code HTML brut (la réponse) en une structure d'objets (une "soupe") dans laquelle on peut naviguer facilement.

## 2. Les Commandes Clés

- **`soup.find('balise', class_='...')`** : Permet de cibler un élément précis dans la page (comme le prix) grâce à son type de balise et sa classe CSS.
- **`.text`** : Permet d'extraire le contenu visible à l'intérieur d'une balise (sans le code HTML autour).

## 3. Nettoyage et Conversion de données

- **`.replace('a', 'b')`** : Remplace le caractère 'a' par 'b'.
  - _Astuce :_ On peut les enchaîner pour tout nettoyer d'un coup.
  - _Exemple :_ `.replace('$', '').replace(',', '')` pour enlever le symbole dollar et la virgule.
- **`float()`** : Convertit une chaîne de caractères (ex: "96000.00") en un nombre décimal (ex: 96000.0) pour pouvoir faire des calculs mathématiques.

## 4. Sauvegarder dans un fichier 💾

- **`open('fichier.txt', 'mode')`** : Ouvre un fichier.
  - Mode `'w'` (Write) : Écrase tout et recommence à zéro.
  - Mode `'a'` (Append) : Ajoute à la suite sans effacer.
- **Le bloc `with`** :
  - Structure : `with open(...) as f:`
  - Rôle : C'est une "zone de sécurité". Le fichier reste ouvert tant qu'on est indenté (décalé) sous le `with`. Dès qu'on en sort, Python ferme et sauvegarde le fichier automatiquement.
- **`f.write(texte)`** : Écrit du texte dans le fichier.
  - _Attention :_ Il faut ajouter `\n` à la fin de la chaîne pour passer à la ligne suivante.
  ## 5. Automatiser le script 🔄
- **`import time`** : Module pour gérer le temps.
  - **`time.sleep(60)`** : Met le programme en "pause" pendant 60 secondes.
- **`while True:`** : Une boucle infinie. Le code à l'intérieur se répétera pour toujours.
- **Arrêt forcé** : Pour arrêter un programme qui tourne à l'infini dans le terminal, on utilise le raccourci clavier **`Ctrl + C`**.

## 6. Visualisation de Données (Data Visualization) 📊

### Installation

Pour tracer des graphiques, on utilise la librairie externe **Matplotlib**.

- **Installation** : `py -m pip install matplotlib`
- **Importation** : `import matplotlib.pyplot as plt`

### Lecture et Nettoyage des Données 🧹

Pour tracer une courbe, il faut transformer les données brutes (texte) en listes utilisables (nombres).

1.  **Lire le fichier** :

    ```python
    with open('fichier.txt', 'r') as f:
        for ligne in f:
            # Action pour chaque ligne
    ```

    - `'r'` : Mode **Read** (lecture seule).
    - `with ... as ...` : Assure la fermeture propre du fichier après utilisation.

2.  **Découper et Convertir** :
    - **`.split(',')`** : Coupe une chaîne de caractères à chaque virgule et crée une liste.
    - **`float(...)`** : Convertit une chaîne de caractères (ex: "10.5") en nombre décimal. **Indispensable** pour que la courbe soit correcte (sinon "100" est classé avant "9").
    - **`.append(...)`** : Ajoute un élément à la fin d'une liste.

### Création du Graphique 📈

On utilise les listes `x` (dates) et `y` (prix) préparées précédemment.

- **`plt.plot(x, y)`** : Trace la courbe (prépare le dessin).
- **`plt.show()`** : Affiche la fenêtre avec le graphique.

### Personnalisation 🎨

- **`plt.title("Mon Titre")`** : Ajoute un titre en haut.
- **`plt.xlabel("Nom axe X")`** : Nomme l'axe horizontal.
- **`plt.ylabel("Nom axe Y")`** : Nomme l'axe vertical.
- **`plt.xticks(rotation=45)`** : Pivote les dates pour éviter qu'elles ne se chevauchent.

## 7. Calculer des Statistiques 🧮

Python possède des fonctions natives pour l'analyse de données simple.

- **Minimum et Maximum** : `min(liste)` et `max(liste)`.
- **Longueur (nombre d'éléments)** : `len(liste)`.
- **Moyenne** : Il faut la calculer à la main (Somme / Total).

**Exemple de code :**

````python
total = 0
for p in prix:
    total += p  # On additionne tous les prix

moyenne = total / len(prix)
print("Prix moyen :", moyenne)

## 8. Le Style et le Design 🎨
Pour rendre le graphique plus professionnel et lisible.

* **La Grille** : `plt.grid(True)` ajoute un quadrillage en fond pour mieux lire les valeurs.
* **Personnaliser la courbe** : On ajoute des options dans `plt.plot()`.
    * `color='red'` : Change la couleur (anglais requis : red, blue, green, black...).
    * `marker='o'` : Ajoute des points sur la ligne ('o' pour rond, 'x' pour croix, etc.).

**Exemple complet :**
```python
plt.grid(True)
plt.plot(dates, prix, color='red', marker='o')
````
