from infrastructure.db.models.user import User
from src.config import db


# En este archivo solo creamos las tablas si no existe. No manejamos la conexion a la, es decir, no abre ni cierra conexiones.

def initialize_db():
    with db:
        # Crea la tabla si no existe
        db.create_tables([User], safe=True)


"""Importa la conexión a la base de datos desde infrastructure.db.
Crea la tabla User si no existe, utilizando el método create_tables.
El bloque if __name__ == "__main__" asegura que la inicialización 
solo se ejecute si ejecutas directamente este archivo (no cuando lo importas desde otro archivo)."""
