# Scanner de Ports TCP en Python

Ce script Python permet de scanner les ports TCP ouverts sur une cible donnée (adresse IP ou nom d'hôte). Il utilise les sockets TCP pour établir des connexions et vérifier si les ports sont accessibles.

## Fonctionnalités

*   Scanne les ports TCP réservés (1 à 1024) par défaut.
*   Utilise le multi-threading pour accélérer le scan (bonus).
*   Gère les erreurs de résolution de nom d'hôte et les interruptions de l'utilisateur.
*   Affiche les ports ouverts de manière claire.

## Prérequis

*   Python >= 3.8

## Utilisation

1.  **Enregistrer le script :** Copiez le code et enregistrez-le dans un fichier nommé `scanner.py`.
2.  **Exécuter :** Ouvrez un terminal et exécutez la commande suivante :

    ```bash
    python3 scanner.py <cible>
    ```

    Remplacez `<cible>` par l'adresse IP ou le nom d'hôte que vous souhaitez scanner.

## Exemple

```bash
python3 scanner.py [www.example.com](https://www.example.com)
