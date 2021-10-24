from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired


class startTest(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired()], render_kw={"placeholder": "Nombre"})
    age_range = SelectField('Selecciona tu rango de edad:',
                              choices=[('', 'Rango de edad'),('Ado', '10-18'), ('Juv', '19-25'),
                                        ('Adu', '26-35'), ('May', '36+')], validators=[InputRequired()],default="''")
    submit = SubmitField('Comenzar')


class quesTest1(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest2(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest3(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest4(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest5(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest6(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest7(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest8(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")

class quesTest9(FlaskForm):
    q1 = SubmitField("Ningún día")
    q2 = SubmitField("Varios días")
    q3 = SubmitField("Más de la mitad de los días")
    q4 = SubmitField("Casi todos los días")