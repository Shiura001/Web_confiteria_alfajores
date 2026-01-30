from flask import request

def procesar_login():
    user = request.form["usuario"]
    return f"Hola {user}"
