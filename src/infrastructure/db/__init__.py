
from peewee import PostgresqlDatabase

# Datos para la conexion a la DB. Creamos un diccionario con los valores de conexion.
DATABASE = {
    'name': 'postgres_db', #nombre de nuestra db
    'user': 'postgres_user', #user de nuestra db
    'password': 'postgres_password', #password de nuestra db
    'host': 'localhost', #Nombre del servidor
    'port': 5432 # puerto por el que se conectara a la db. En este caso es el puerto que utiliza postgres.
}

# Conexion a DB. Utilizamos los datos necesarios para la conexion.
#Instancia de PostgresqlDatabase que usa los valores definidos en el diccionario DATABASE.
db = PostgresqlDatabase(
    DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)
