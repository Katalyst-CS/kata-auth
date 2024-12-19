# Archivo: src/config.py

from peewee import PostgresqlDatabase

# Datos de configuración de la base de datos
DATABASE = {
    'name': 'postgres_db',  # Nombre de la base de datos
    'user': 'postgres_user',  # Usuario de la base de datos
    'password': 'postgres_password',  # Contraseña del usuario
    'host': 'localhost',  # Dirección del servidor de la base de datos
    'port': 5432  # Puerto en el que está escuchando PostgreSQL
}

# Instancia de conexión a la base de datos
db = PostgresqlDatabase(
    DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)

# Función para conectar a la base de datos
def connect_to_database():
    """
    Abre la conexión con la base de datos.
    """
    if db.is_closed():
        db.connect()


# Función para cerrar la conexión a la base de datos

def close_database_connection():
    """
    Cierra la conexión con la base de datos si está abierta.
    """
    if not db.is_closed():
        db.close()