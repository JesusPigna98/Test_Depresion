from flask import Flask, render_template, url_for, redirect
from forms import startTest


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
        subm = form.submit.data
        print(name, age, subm)
        return redirect(url_for('test'))

    return render_template('index.html', form=form)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/results')
def results():
    pass










############################################

        # MAIN

##########################################
if __name__ == '__main__':
    app.run(debug=True)