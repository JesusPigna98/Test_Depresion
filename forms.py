from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired


class startTest(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired()], render_kw={"placeholder": "Nombre"})
    age_range = SelectField('Selecciona tu rango de edad:',
                              choices=[('', 'Rango de edad'),('Ado', '10-18'), ('Juv', '19-25'),
                                        ('Adu', '26-35'), ('May', '36+')], validators=[InputRequired()],default="''")
    submit = SubmitField('Comenzar')

