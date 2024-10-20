# Archivo: app/models/user_model.py
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Nueva columna para la contraseña hasheada
    password_hash = db.Column(db.String(128), nullable=False)
    # Nueva columna para el rol del usuario
    role = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        """Hashea la contraseña y la almacena"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si la contraseña proporcionada coincide con la hasheada"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username} - Role: {self.role}>'

# Opcionales: Define constantes para los roles
ADMINISTRATOR = 'Administrador'
TEACHER = 'Maestro'
SUPERVISOR = 'Supervisor'

# Ejemplo de cómo agregar un usuario con un rol específico
user1 = User(username='alice', email='alice@example.com', role=ADMINISTRATOR)
