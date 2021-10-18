from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class startTest(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired()])
    age_range = SelectField('Selecciona tu rango de edad:',
                              choices=[('Ado', '10-18'), ('Juv', '19-25'),
                                        ('Adu', '26-35'), ('May', '36+')])
    submit = SubmitField('Comenzar Test')

