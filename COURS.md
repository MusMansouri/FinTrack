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
