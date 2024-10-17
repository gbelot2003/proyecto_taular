# Archivo: app/__init__.py

from flask import Flask
from app.models import db  # Importa la instancia centralizada de la base de datos
from config import DevelopmentConfig  # Importa la configuración adecuada

def create_app(config_class=DevelopmentConfig):
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Cargar la configuración desde config.py
    app.config.from_object(config_class)

    # Inicializa la base de datos con la aplicación Flask
    db.init_app(app)

    # Crear las tablas de la base de datos si no existen
    with app.app_context():
        db.create_all()

    return app
