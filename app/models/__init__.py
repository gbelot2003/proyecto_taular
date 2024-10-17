# Archivo: models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Inicializa la instancia de la base de datos
db = SQLAlchemy()

# Importar todos los modelos aquí para que sean registrados con SQLAlchemy
from .user_model import User
from .grado_model import Grado
from .clase_model import Clase
from .alumno_model import Alumno
from .parcial_model import Parcial
from .tarea_model import Tarea
from .prueba_model import Prueba
from .examen_model import Examen