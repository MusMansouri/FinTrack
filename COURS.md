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
