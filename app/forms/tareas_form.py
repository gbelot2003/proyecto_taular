from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from app.models.parcial_model import Parcial
from app.models.alumno_model import Alumno

class TareaForm(FlaskForm):
    descripcion = StringField('Descripción de la Tarea', validators=[DataRequired()])
    parcial = SelectField('Parcial', coerce=int, validators=[DataRequired()])
    alumno = SelectField('Alumno', coerce=int, validators=[DataRequired()])
    puntaje_maximo = FloatField('Puntaje Máximo', validators=[DataRequired(), NumberRange(min=0, max=100)])
    # Hacemos que puntaje obtenido no sea obligatorio al crear
    puntaje_obtenido = FloatField('Puntaje Obtenido', validators=[NumberRange(min=0, max=100)], default=None)
    submit = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        # Rellenar los campos con los datos de Parciales y Alumnos
        self.parcial.choices = [(p.id, f"Parcial {p.numero} - {p.clase.nombre}") for p in Parcial.query.all()]
        self.alumno.choices = [(a.id, f"{a.nombre} {a.apellido}") for a in Alumno.query.all()]
