from flask import Flask
from app.models import db  # Importa la instancia centralizada de la base de datos
from config import DevelopmentConfig  # Importa la configuración adecuada

app = Flask(__name__)

# Cargar la configuración desde el archivo config.py
app.config.from_object(DevelopmentConfig)  # Carga la configuración de desarrollo

# Inicializa la base de datos con la aplicación Flask
db.init_app(app)

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
