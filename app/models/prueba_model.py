# Archivo: app/models/prueba_model.py

from . import db
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class Prueba(db.Model):
    __tablename__ = 'pruebas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)  # Descripción de la prueba
    puntaje_maximo = db.Column(db.Float, nullable=False)  # Puntaje máximo de la prueba
    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)

    # Relación con Parcial y Alumno
    parcial = db.relationship('Parcial', backref='pruebas')
    alumno = db.relationship('Alumno', backref='pruebas')

    # Puntaje obtenido por el alumno
    puntaje_obtenido = db.Column(db.Float, nullable=True)

    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)
    parcial = db.relationship('Parcial', backref='pruebas')

    def __repr__(self):
        return f'<Prueba {self.descripcion} para el Alumno {self.alumno.nombre}>'
