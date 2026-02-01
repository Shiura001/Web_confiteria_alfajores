from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de SQLAlchemy aquí
db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    sabor = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)