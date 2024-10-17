from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class UserForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    role = SelectField('Rol', choices=[('admin', 'Administrador'), ('teacher', 'Maestro'), ('student', 'Estudiante')], validators=[DataRequired()])
    submit = SubmitField('Guardar')
