# Archivo: app/models/examen_model.py

from . import db
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class Examen(db.Model):
    __tablename__ = 'examenes'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)  # Descripción del examen
    puntaje_maximo = db.Column(db.Float, nullable=False)  # Puntaje máximo para el examen
    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)

    # Relación con Parcial y Alumno
    parcial = db.relationship('Parcial', backref='examenes')
    alumno = db.relationship('Alumno', backref='examenes')

    # Puntaje obtenido por el alumno
    puntaje_obtenido = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Examen {self.descripcion} para el Alumno {self.alumno.nombre}>'
