# 📈 Visualisation du Prix du Bitcoin

Ce projet est un script Python qui analyse l'évolution du prix du Bitcoin à partir d'un fichier de données historiques. Il génère une courbe visuelle et calcule des statistiques clés.

## 📋 Fonctionnalités

* **Lecture de données** : Importation des données depuis un fichier texte brut (`bitcoin_history.txt`).
* **Nettoyage** : Conversion des types de données pour l'analyse.
* **Visualisation** : Création d'un graphique avec **Matplotlib** (courbe, points, grille).
* **Statistiques** : Calcul et affichage du prix minimum, maximum et moyen dans la console.
* **Export** : Sauvegarde automatique du graphique au format image (`.png`).

## 🛠️ Prérequis

Pour lancer ce projet, vous avez besoin de :
* Python 3.x installé.
* La librairie **Matplotlib**.

## 🚀 Installation et Utilisation

1.  **Cloner le projet** (ou télécharger les fichiers).
2.  **Installer les dépendances** :
    Ouvrez votre terminal et tapez :
    ```bash
    py -m pip install matplotlib
    ```
3.  **Lancer le script** :
    ```bash
    py visualisation.py
    ```

## 📊 Résultat

Une fois le script lancé :
1.  Une fenêtre s'ouvre avec la courbe d'évolution.
2.  Les statistiques s'affichent dans le terminal.
3.  Une image `courbe_bitcoin.png` est générée dans le dossier.

---
*Projet réalisé dans le cadre de mon apprentissage Python.*
