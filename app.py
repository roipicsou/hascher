from flask import Flask, render_template, request, redirect, url_for
import os
from hashlib import sha256

app = Flask(__name__)
chemin = "/media/root/disque_dure1/"

def liste_dosier(dossier) :
    fichiers = os.listdir(dossier)
    
    # Filtrer uniquement les fichiers (exclure les répertoires)
    fichiers = [os.path.join(dossier, fichier) for fichier in fichiers if os.path.isfile(os.path.join(dossier, fichier))]
    
    return fichiers

def get_mdp(mdp) :
    with open("/media/root/disque_dure/bob.txt", "r") as fichier:
        hash1 = fichier.read()
    moddepasse = sha256(mdp.encode('utf-8')).hexdigest() + "\n"
    print()
    if moddepasse == hash1 :
        return True
    else :
        return False

def chiffrer(chemin, mdp) :
    os.system(f"gpg --batch --yes --passphrase {mdp}  --symmetric {chemin}")
    os.system(f"rm {chemin}")

def extracte(fichier) :
    if '.' in fichier:
        return '.'.join(fichier.split('.')[:-1])
    return fichier

def dechifréer(chemin, mdp) :
    os.system(f"gpg --batch --yes --passphrase {mdp} --decrypt {chemin} > {extracte(chemin)}")
    os.system(f"rm {chemin}")

# Page principale
@app.route('/')
def index():
    return render_template('index.html')

# Route pour exécuter une fonction directement
@app.route('/action1')
def action1():
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
    if get_mdp(param1) and param2 == "chyfrée":
        result = liste_dosier(chemin)
        for i in result :
            chiffrer(i, param1)
    elif get_mdp(param1) and param2 == "dechifréer" :
        pass
    else :
        result = "eror mdp"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)