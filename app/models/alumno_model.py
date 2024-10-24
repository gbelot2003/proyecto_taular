# Archivo: app/models/alumno_model.py

from . import db
from app.models.grado_model import Grado

class Alumno(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    grado_id = db.Column(db.Integer, db.ForeignKey('grados.id'), nullable=False)
    grado = db.relationship('Grado', backref='alumnos')

    tareas = db.relationship('Tarea', back_populates='alumno', lazy=True)
    examenes = db.relationship('Examen', back_populates='alumno', lazy=True)

    def __repr__(self):
        return f'<Alumno {self.nombre} {self.apellido} - Grado: {self.grado.nombre}>'

