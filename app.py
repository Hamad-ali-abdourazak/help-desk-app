from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Remplacez cette URL par l'URL de votre Logic App
LOGIC_APP_URL = "https://prod-20.francecentral.logic.azure.com:443/workflows/dff0d71593a84b8e9a67e3a7d28123df/triggers/When_a_HTTP_request_is_received/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2FWhen_a_HTTP_request_is_received%2Frun&sv=1.0&sig=HiO37VGTnNQTfKFx7JqrdujV7IsGNannE6dTGkEP4EI"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Récupérer les données du formulaire
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Vérification de la présence des champs
        if not name or not email or not message:
            return jsonify({"status": "error", "message": "Tous les champs sont requis"})

        # Préparer les données à envoyer à la Logic App
        data = {"name": name, "email": email, "message": message}

        # Envoyer les données à la Logic App via une requête POST
        response = requests.post(LOGIC_APP_URL, json=data)

        # Vérifier la réponse de la Logic App
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Demande envoyée avec succès à la Logic App"})
        elif response.status_code == 202:  # Ajoutez cette condition pour accepter également le code 202
            return jsonify({"status": "success", "message": "Demande acceptée par la Logic App"})
        else:
            return jsonify({"status": "error", "message": f"Erreur lors de l'envoi à la Logic App : {response.status_code} - {response.text}"})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Erreur interne du serveur : {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)


