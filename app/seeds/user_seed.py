# Archivo: user_seed.py
from app import db, app  # Importar desde 'app.py'
from app.models.user_model import User

def seed_data():
    with app.app_context():
        # Crear algunos usuarios
        user1 = User(username='alice', email='alice@example.com')
        user2 = User(username='bob', email='bob@example.com')
        user3 = User(username='charlie', email='charlie@example.com')

        # Agregar usuarios a la sesión
        db.session.add_all([user1, user2, user3])
        db.session.commit()

        print("Seeding completado.")

if __name__ == '__main__':
    seed_data()
