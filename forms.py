from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired


class startTest(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired()], render_kw={"placeholder": "Nombre"})
    age_range = SelectField('Selecciona tu rango de edad:',
                              choices=[('', 'Rango de edad'),('Adolescente', '10-18'), ('Juventud', '19-25'),
                                        ('Adultez', '26-35'), ('Maduro', '36+')], validators=[InputRequired()],default="''")
    submit = SubmitField('Comenzar')


class final(FlaskForm):
    submit = SubmitField('Finalizar')