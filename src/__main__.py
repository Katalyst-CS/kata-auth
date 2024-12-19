# Archivo: src/app.py

from flask import Flask, jsonify

from config import connect_to_database, close_database_connection
from initialize_db import initialize_db
from .infrastructure.db.models.user import User

# Crear la aplicación Flask
app = Flask(__name__)


# Ruta para listar usuarios
@app.route("/users", methods=["GET"])
def list_users():
    """
    Endpoint que retorna la lista de usuarios en formato JSON.
    """
    users = User.select()  # Consulta todos los usuarios
    users_list = [
        {"id": user.id, "username": user.username, "email": user.email, "created_at": user.created_at}
        for user in users
    ]
    return jsonify(users_list)


# Punto de entrada de la aplicación
if __name__ == "__main__":
    connect_to_database()  # Conectar a la base de datos
    try:
        initialize_db()  # Inicializar las tablas en la base de datos
        app.run(debug=True, port=5000)  # Iniciar la aplicación Flask
    finally:
        close_database_connection()  # Cerrar la conexión a la base de datos
