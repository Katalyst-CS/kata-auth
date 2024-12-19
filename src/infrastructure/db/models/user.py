
from peewee import *
import datetime

from src.config import db


class User(Model):
    username = CharField(unique=True, max_length=50)
    email = CharField(unique=True, max_length=100)
    password = CharField(max_length=100)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db  # Indica que este modelo usa la base de datos definida en db_connection