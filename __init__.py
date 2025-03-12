from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template('contact.html')

@app.route('/carre/<int:val>')
def carre(val):
    return "<h2>Le carré de la valeur est : </h2>" + str(val*val)

@app.route('/somme/<int:val1>/<int:val2>')
def somme(val1,val2):
    return "<h2>La somme de vos valeurs est : </h2>" + str(val1+val2)

@app.route('/parite/<int:val>')
def parite(val):
    if val%2==0:
        return "La valeur que vous avez donné est paire"
    else:
        return "La valeur que vous avez donné est impaire"

@app.route('/sommetotale/<path:val>')
def sommetot(val):
    sommet = list(map(int, val.split('/')))
    sommetotale = sum(sommet)
    return "La somme totale des valeurs est : " + str(sommetotale)

@app.route('/sommemax/<path:val>')
def sommemax(val):
    sommet = list(map(int, val.split('/')))
    compare = 0
    for i in range(len(sommet)):
        if (compare-sommet[i]>=0):
            break
        else:
            compare=sommet[i]
    return "La valeur max est :" + str(compare)

@app.route('/cnam/')
def cnampage():
    return render_template('cnam.html')

@app.route("/exercice_base1/")
def exo1():
    return render_template('exercice_base1.html')

@app.route("/exercice_base2/")
def exo2():
    return render_template('exercice_base2.html')

@app.route("/formulaire/")
def exo4():
    return render_template('formulaire.html')

@app.route("/TP1/")
def tp1():
    return render_template('TP1.html')

@app.route("/actualite/")
def actualite():
    return render_template('actualite.html')

@app.route("/page1/")
def page1():
    return render_template('page1.html')

@app.route("/page2/")
def page2():
    return render_template('page2.html')

@app.route("/page3/")
def page3():
    return render_template('page3.html')

@app.route("/cv/")
def cv():
    return render_template('cv.html')

@app.route("/maison/")
def Exemple_Base_SVG():
    return render_template('Exemple_Base_SVG.html')

@app.route("/valet/")
def valet():
    return render_template('valet.html')

@app.route("/chenille/")
def chenille():
    return render_template('chenille.html')

@app.route("/carre/")
def CSS_Carre():
    return render_template('CSS_Carre.html')

@app.route("/etoiles/")
def etoiles():
    return render_template('Carre_Etoiles.html')

@app.route("/images/")
def images():
    return render_template('images.html')

@app.route("/Jeu_Des/")
def Jeu_Des_Base():
    return render_template('Jeu_Des_Base.html')


if __name__ == "__main__":
  app.run(debug=True)
