from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/for/')
def html_index():
    context = {
        'title': 'Цикл',
        'poem': ['Вот не думал, не гадал,',
                 'Программистом взял и стал.',
                 'Python знает он язык,',
                 'Дальше с рифмой не дружу.']
    }
    return render_template('show_if.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
