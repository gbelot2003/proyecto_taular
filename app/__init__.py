# Archivo: app/__init__.py

from flask import Flask
from app.models import db  # Importa la instancia centralizada de la base de datos
from config import DevelopmentConfig  # Importa la configuración adecuada
from flask_migrate import Migrate
from app.routes.router import configure_routes
from flask_socketio import SocketIO

def create_app(config_class=DevelopmentConfig):
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Cargar la configuración desde config.py
    app.config.from_object(config_class)

    # Inicializa la base de datos con la aplicación Flask
    db.init_app(app)

    # Inicializar Flask-Migrate
    migrate = Migrate(app, db)

    socketio = SocketIO(app,  cors_allowed_origins="*")

    # Configura las rutas
    configure_routes(app, socketio)

    return app