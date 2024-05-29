from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.get('/submit')
def submit_get():
    return render_template('form.html')


@app.post('/submit')
def submit_post():
    name = request.form['name']
    return f'Hello, {name.capitalize()}!'


if __name__ == '__main__':
    app.run(debug=True)
