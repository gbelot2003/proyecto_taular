# Archivo: models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Inicializa la instancia de la base de datos
db = SQLAlchemy()

# Importar todos los modelos aquí para que sean registrados con SQLAlchemy
from .user_model import User
from .grado_model import Grado
