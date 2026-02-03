from flask import Flask, render_template, request, redirect, url_for
from Modulos.logear import procesar_login
from models.model import db, Pedido
import os
from Modulos.procesar_pedido import verificar_pedido
app = Flask(__name__)
app.secret_key = 'una_clave_muy_secreta_y_larga_12345'
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

@app.route('/procesar_pedido', methods=['POST'])
def mi_logica_de_pedido():
    # Aquí es donde Flask recibe los datos del formulario
    nombre = request.form.get('cliente')
    # Convertimos a entero para poder multiplicar
    cantidad = int(request.form.get('cantidad')) 
    total = cantidad * 12
    return render_template('tus_pedidos.html', nombre=nombre, total=total)



# base de datos
# Configuración inteligente (Render o Local)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///maicenita.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Unimos la base de datos con la App
db.init_app(app)

# Creamos las tablas si no existen
with app.app_context():
    db.create_all()

@app.route('/procesar_pedido1', methods=['POST'])
def nuevo_pedido():
    return verificar_pedido()
 
    


@app.route('/pedidos')

def ver_pedidos():
    # Traemos todos los pedidos de la base de datos
    lista_pedidos = Pedido.query.all()
    
    # Enviamos la lista al archivo HTML
    return render_template('lista.html', pedidos=lista_pedidos)




if __name__ == "__main__":
    app.run(debug=True)
