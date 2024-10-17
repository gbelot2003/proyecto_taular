# Archivo: app/seeds/clase_seed.py
import sys
import os

# Asegurarse de que el directorio raíz del proyecto está en sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import create_app, db
from app.models.grado_model import Grado
from app.models.clase_model import Clase

def seed_clases():
    app = create_app()  # Crear la aplicación Flask
    with app.app_context():
        # Obtener los grados
        primero = Grado.query.filter_by(nombre='Septimo A').first()
        
        # Crear algunas clases y asignarlas a grados
        clase1 = Clase(nombre='Matemáticas', grado=primero)
        clase2 = Clase(nombre='Historia', grado=primero)
        clase3 = Clase(nombre='Ciencias', grado=primero)
        clase4 = Clase(nombre='Geografía', grado=primero)

        # Agregar las clases a la sesión
        db.session.add_all([clase1, clase2, clase3, clase4])
        db.session.commit()

        print("Seeding completado: Clases agregadas.")

if __name__ == '__main__':
    seed_clases()
