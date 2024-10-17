from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TimeField, SubmitField
from wtforms.validators import DataRequired
from app.models.grado_model import Grado
from app.models.user_model import User

class ClaseForm(FlaskForm):
    nombre = StringField('Nombre de la clase', validators=[DataRequired()])
    grado = SelectField('Grado', coerce=int, validators=[DataRequired()])
    maestro = SelectField('Maestro', coerce=int, validators=[DataRequired()])
    horario_inicio = TimeField('Horario de inicio', validators=[DataRequired()])
    horario_fin = TimeField('Horario de fin', validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super(ClaseForm, self).__init__(*args, **kwargs)
        # Rellenar los campos con los datos de Grados y Maestros
        self.grado.choices = [(g.id, g.nombre) for g in Grado.query.order_by(Grado.nombre).all()]
        self.maestro.choices = [(u.id, u.username) for u in User.query.filter_by(role='teacher').order_by(User.username).all()]
