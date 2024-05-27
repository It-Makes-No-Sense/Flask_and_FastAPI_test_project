from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/users/')
def html_index():
    _users = [
        {
            'name': 'Глеб',
            'mail': 'gleb@mail.ru',
            'phone': '+7-917-222-12-32'},
        {
            'name': 'Влад',
            'mail': 'vlad@mail.ru',
            'phone': '+7-917-222-12-32'
        },
        {
            'name': 'Андрей',
            'mail': 'andrey@mail.ru',
            'phone': '+7-917-222-12-32'
        },

    ]
    context = {'users': _users,
               'title': 'Точечная информация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
