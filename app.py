from flask import Flask, render_template, url_for, redirect, request, session
from forms import startTest,final


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


############################################

        # VIEWS WITH FORMS

##########################################

@app.route('/', methods=['GET','POST'])
def index():
    form = startTest()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age_range.data
        session['name'] = name
        session['age'] = age

        # subm = form.submit.data
        # subm3 = form.submit._value()
        print(name, age)
        return redirect(url_for('test'))

    return render_template('index.html', form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    form= final()

    if form.validate_on_submit():
        option1 = int(request.form['q1'])
        option2 = int(request.form['q2'])
        option3 = int(request.form['q3'])
        option4 = int(request.form['q4'])
        option5 = int(request.form['q5'])
        option6 = int(request.form['q6'])
        option7 = int(request.form['q7'])
        option8 = int(request.form['q8'])
        option9 = int(request.form['q9'])
        total = option1+option2+option3+option4+option5+option6+option7+option8+option9
        session['total'] = total
        

        return redirect(url_for('results'))

    # if pregunta1.is_submitted():
    #     val_depresion = 0
    #     procesado(pregunta1, val_depresion)    

    return render_template('test.html',form=form)



@app.route('/results')
def results():
    name = session.get('name',None)
    age = session.get('age',None)
    total = session.get('total',None)

    return render_template('results.html', name=name,age=age,total=total)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


############################################

        # MAIN

##########################################
if __name__ == '__main__':
    app.run(debug=True)