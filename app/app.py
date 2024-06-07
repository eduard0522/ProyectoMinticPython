""" APP-MINTIC """
from flask import Flask,url_for,render_template
from files import filterData
app = Flask(__name__)
app = Flask(__name__, template_folder="../src/templates", static_folder="../src/static")

@app.route("/")
def index():
    """ ruta principal """
    print(url_for("index"))
    print(url_for("cundinamarca"))
    print(url_for("boyaca"))
    return render_template('index.html')

@app.route("/cundinamarca")
def cundinamarca():
    """ Maneja las solicitudes a la ruta cundinamarca """
    datos = filterData('cundina')
    return render_template("cundinamarca.html",data = datos)

@app.route("/boyaca.hmtl")
def boyaca():
    """ Maneja las solicitudes a la ruta Boyacá """
    datos = filterData('boyac')
    return render_template("boyaca.html", data = datos)

if __name__  ==  '__main__':
    app.run(debug=True)
