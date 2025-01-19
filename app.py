from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Page principale
@app.route('/')
def index():
    return render_template('index.html')

# Route pour exécuter une fonction directement
@app.route('/action1')
def action1():
    chemin = "/media/root/disque_dure1/"
    if os.path.isdir(chemin):
        result = "Le desier existe"
    else:
        result = "Le doiser n'existe pas"
    return render_template('result.html', result=result)

# Route pour rediriger vers une page avec des paramètres
@app.route('/parameters')
def parameters():
    return render_template('parameters.html')

# Route pour traiter les paramètres soumis
@app.route('/process_parameters', methods=['POST'])
def process_parameters():
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')
    result = f"Paramètres reçus : {param1}, {param2}"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)