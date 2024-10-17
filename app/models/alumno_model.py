# Archivo: app/models/alumno_model.py

from . import db
from app.models.grado_model import Grado

class Alumno(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del alumno
    apellido = db.Column(db.String(100), nullable=False)  # Apellido del alumno
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email del alumno

    # Relación con Grado (un alumno pertenece a un grado)
    grado_id = db.Column(db.Integer, db.ForeignKey('grados.id'), nullable=False)
    grado = db.relationship('Grado', backref='alumnos')

    def __repr__(self):
        return f'<Alumno {self.nombre} {self.apellido} - Grado: {self.grado.nombre}>'
