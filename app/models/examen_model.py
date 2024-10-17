# Archivo: app/models/examen_model.py

from . import db
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class Examen(db.Model):
    __tablename__ = 'examenes'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    puntaje_maximo = db.Column(db.Float, nullable=False)
    puntaje_obtenido = db.Column(db.Float)

    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    parcial_id = db.Column(db.Integer, db.ForeignKey('parciales.id'), nullable=False)

    alumno = db.relationship('Alumno', back_populates='examenes')
    parcial = db.relationship('Parcial', backref='examenes')

    def __repr__(self):
        return f'<Examen {self.descripcion} - Alumno {self.alumno.nombre}>'

