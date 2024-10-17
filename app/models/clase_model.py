# Archivo: app/models/clase_model.py

from . import db
from app.models.grado_model import Grado
from app.models.user_model import User
from datetime import time

class Clase(db.Model):
    __tablename__ = 'clases'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nombre de la clase
    
    # Relación con Grado (una clase pertenece a un grado)
    grado_id = db.Column(db.Integer, db.ForeignKey('grados.id'), nullable=False)
    grado = db.relationship('Grado', backref='clases')

    # Relación con User (una clase tiene un maestro)
    maestro_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    maestro = db.relationship('User', backref='clases')

    # Campos para el horario de la clase
    horario_inicio = db.Column(db.Time, nullable=False)  # Hora de inicio de la clase
    horario_fin = db.Column(db.Time, nullable=False)  # Hora de fin de la clase

    def __repr__(self):
        return f'<Clase {self.nombre} - Grado: {self.grado.nombre} - Maestro: {self.maestro.username}>'
