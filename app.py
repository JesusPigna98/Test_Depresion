from flask import Flask, render_template, url_for, redirect
from forms import (startTest, quesTest1, quesTest2, quesTest3, quesTest4, quesTest5,
                  quesTest6, quesTest7, quesTest8, quesTest9)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # VIEWS WITH FORMS

##########################################


def procesado(pregunta, val_depresion):
    print(pregunta.q1.data,pregunta.q2.data,pregunta.q3.data,pregunta.q4.data)
    if pregunta.q1.data:
        val_depresion += 0

    if pregunta.q2.data:
        val_depresion += 1
        print(val_depresion)
    
    elif pregunta.q3.data:
        val_depresion += 2
        print(val_depresion)
    
    elif pregunta.q4.data:
        val_depresion += 3
        print(val_depresion)


@app.route('/', methods=['GET','POST'])
def index():
    form = startTest()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age_range.data
        subm = form.submit.data
        subm3 = form.submit._value()
        print(name, age, subm, subm3)
        return redirect(url_for('test'))

    return render_template('index.html', form=form)

@app.route('/test', methods=['GET', 'POST'])
def test():
    pregunta1 = quesTest1()
    pregunta2 = quesTest2()
    # pregunta3 = quesTest3()
    # pregunta4 = quesTest4()
    # pregunta5 = quesTest5()
    # pregunta6 = quesTest6() 
    # pregunta7 = quesTest7()
    # pregunta8 = quesTest8()
    # pregunta9 = quesTest9()

    # procesado(quesTest1,quesTest2,quesTest3,quesTest4,
    #           quesTest5,quesTest6,quesTest7,quesTest8,quesTest9)   

    # if pregunta1.is_submitted():
    #     val_depresion = 0
    #     procesado(pregunta1, val_depresion)    

    return render_template('test.html', pregunta1=pregunta1, pregunta2=pregunta2)

@app.route('/results')
def results():
    render_template('results.html')



############################################

        # MAIN

##########################################
if __name__ == '__main__':
    app.run(debug=True)