# Help Desk App

C'est une application qui permet de gérer le support clients. Elle a été développée avec Flask et HTML. Le projet utilise également une Logic App, un Blob Storage et une Web App d'Azure. De plus, l'application envoie un email lorsque le client soumet son nom, email et message détaillant son problème.

## Prérequis

- Python 3.x
- Flask
- Requests

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/help-desk-app.git
    cd help-desk-app
    ```

2. Installez les dépendances :
    ```sh
    python -m pip install flask requests
    ```

## Utilisation

1. Ajoutez le code suivant à la fin de votre fichier [`app.py`] pour démarrer le serveur Flask :
    ```python
    if __name__ == "__main__":
        app.run(debug=True)
    ```

2. Lancez l'application en exécutant le fichier [app.py] :
    ```sh
    python app.py
    ```

3. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

## Déploiement

L'application est déployée sur Azure en utilisant une Logic App, un Blob Storage et une Web App. Suivez les étapes de la documentation Azure pour déployer votre application Flask.

## Fonctionnalités

- Soumission de demandes de support via un formulaire.
- Envoi des données à une Logic App pour traitement.
- Stockage des données dans un Blob Storage.
- Envoi d'un email de notification avec les détails du problème soumis par le client.
- Interface utilisateur simple et intuitive.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [`LICENSE`] pour plus de détails.
