# AHA - Calculator

AHA Calculator est une calculatrice simple et élégante construite avec **PySide6** (Qt pour Python). Elle offre une interface graphique utilisateur pour effectuer des calculs de base et des opérations arithmétiques. Ce projet inclut également des effets visuels pour les boutons et la gestion des erreurs de calcul.

## Fonctionnalités

- **Opérations de base** : addition, soustraction, multiplication, division.
- **Effet visuel sur les boutons** : changement de couleur au survol et à l'appui.
- **Réinitialisation de l'affichage** : via le bouton "CE".
- **Gestion des erreurs** : gestion des erreurs comme la division par zéro.
- **Interface utilisateur conviviale** avec un affichage clair des résultats.

## Prérequis

Avant d'exécuter ce projet, vous devez avoir installé **Python 3.x** et la bibliothèque **PySide6**.

### Installer les dépendances

1. Clonez ce repository sur votre machine locale :

   ```bash
   git clone https://github.com/HafizAdib/Calculator.git
   ```

2. Accédez au dossier du projet :

   ```bash
   cd Calculator
   ```

3. Installez les dépendances nécessaires avec **pip** :

   ```bash
   pip install PySide6
   ```

## Utilisation

1. Une fois l'installation terminée, vous pouvez exécuter l'application en lançant le script principal `main.py` :

   ```bash
   python main.py
   ```

2. L'application s'ouvrira avec une interface graphique contenant un champ d'affichage pour vos calculs et des boutons pour les chiffres et les opérations.

3. Vous pouvez interagir avec la calculatrice en utilisant les boutons suivants :
   - **Chiffres** : cliquez sur les chiffres pour les ajouter à l'affichage.
   - **Opérations** : utilisez les boutons `+`, `-`, `x`, `/` pour effectuer des calculs.
   - **CE** : réinitialise l'affichage.
   - **=** : affiche le résultat du calcul.
   - **Gestion des erreurs** : en cas d'erreur, un message "ERREUR" sera affiché.

## Exemple de code pour calculer et gérer les erreurs

Voici un extrait de code qui montre comment la fonction de calcul est implémentée et comment les erreurs sont gérées :

```python
def calculate(self):
    try:    
        solution = eval(self.display.text())  # Calcul de l'expression
        self.display.setText(f"= {solution}")  # Affiche le résultat
    except(SyntaxError, NameError, ZeroDivisionError):
        self.display.setText(f"ERREUR")  # Gère les erreurs
```

### Explication :
- **`eval()`** est utilisé pour évaluer l'expression mathématique dans l'affichage.
- Si une erreur est détectée (comme une division par zéro ou une erreur de syntaxe), le message "ERREUR" sera affiché.

## Exemple d'interface

L'interface utilisateur est composée des éléments suivants :
- **Affichage** : un champ de texte en haut pour afficher les calculs et résultats.
- **Boutons** : pour les chiffres, les opérations, ainsi que les boutons fonctionnels ("CE", "=").

Le style visuel est simple, avec des effets de survol et d'appui pour les boutons, ce qui améliore l'expérience utilisateur.

---

## Aide et Support

Je suis toujours present pour les conseils d'ameliorationde ce mini projet, n'hésitez pas à ouvrir une **issue** sur GitHub ou à me contacter directement.

Merci d'utiliser AHA Calculator !
