# Archivo: test_app.py

import unittest
from run import app
from app.models import db, User
from config import TestingConfig

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación para el entorno de pruebas
        app.config.from_object(TestingConfig)
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Crear todas las tablas
        db.create_all()

    def tearDown(self):
        # Eliminar las tablas después de cada prueba
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        # Crear un nuevo usuario
        user = User(username='testuser', email='testuser@example.com')
        db.session.add(user)
        db.session.commit()

        # Verificar si el usuario se creó correctamente
        queried_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'testuser@example.com')

if __name__ == '__main__':
    unittest.main()
