from flask import request, redirect, url_for,flash
from models.model import db, Pedido

def verificar_pedido():
    cliente = request.form["cliente"]
    sabor = request.form["sabor"]
    cantidad = int(request.form["cantidad"])

    if not cliente or not sabor:
        flash("¡Cuidado! Todos los campos son obligatorios.", "error") # "error" es la categoría
        return redirect(url_for('home'))
    
    if cantidad == 0:
        flash("Cantidad debe ser mayor a 0 amigo :v.", "error") # "error" es la categoría
        return redirect(url_for('servicios'))

    pedido = Pedido(
        cliente=request.form.get('cliente'),
        sabor=request.form.get('sabor'),
        cantidad=int(request.form.get('cantidad'))
    )
    db.session.add(pedido)
    db.session.commit()
    return redirect(url_for('ver_pedidos'))

    
