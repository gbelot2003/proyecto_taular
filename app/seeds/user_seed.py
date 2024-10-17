import sys
import os

# Asegurarse de que el directorio raíz del proyecto está en sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import create_app, db
from app.models.user_model import User, ADMINISTRATOR, TEACHER

def seed_data():
    app = create_app()  # Crear la aplicación Flask
    with app.app_context():
        # Crear el usuario administrador
        admin_user = User(username='admin', email='admin@example.com', role=ADMINISTRATOR)

        # Crear algunos usuarios maestros
        teacher1 = User(username='teacher1', email='teacher1@example.com', role=TEACHER)
        teacher2 = User(username='teacher2', email='teacher2@example.com', role=TEACHER)
        teacher3 = User(username='teacher3', email='teacher3@example.com', role=TEACHER)

        # Agregar los usuarios a la sesión
        db.session.add_all([admin_user, teacher1, teacher2, teacher3])
        db.session.commit()

        print("Seeding completado: Usuarios agregados.")

if __name__ == '__main__':
    seed_data()