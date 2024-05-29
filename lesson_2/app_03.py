from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/about/')
def about():
    contex = {
        'title': 'Обо мне',
        'name': 'Гриша',
    }
    return render_template('about.html', **contex)


if __name__ == '__main__':
    app.run(debug=True)
