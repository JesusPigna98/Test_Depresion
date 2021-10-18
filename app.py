from flask import Flask, render_template, request, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # VIEWS WITH FORMS

##########################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    pass

@app.route('results')
def results():
    pass










############################################

        # MAIN

##########################################
if __name__ == '__main__':
    app.run(Debug=True)