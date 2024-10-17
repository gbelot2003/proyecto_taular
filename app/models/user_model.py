# Archivo: app/models/user_model.py

from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Nueva columna para el rol del usuario
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username} - Role: {self.role}>'

# Opcionales: Define constantes para los roles
ADMINISTRATOR = 'Administrador'
TEACHER = 'Maestro'
SUPERVISOR = 'Supervisor'

# Ejemplo de cómo agregar un usuario con un rol específico
user1 = User(username='alice', email='alice@example.com', role=ADMINISTRATOR)
