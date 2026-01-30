from flask import Flask, render_template, request, redirect, url_for
from Modulos.logear import procesar_login
app = Flask(__name__)

# Ruta Home
@app.route("/")
def home():
    return render_template("home.html")  # Página de bienvenida

# Ruta Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return procesar_login()
    return render_template("login.html")  

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == "__main__":
    app.run(debug=True)
