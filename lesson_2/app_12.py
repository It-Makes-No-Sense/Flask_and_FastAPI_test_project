from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'99f3f1b11f29c1ca79f9cda98c9e071539e5c33b61854916ea1fa64bdffc6cac'
"""
Генерация надежного секретного ключа:
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        if not request.form.get('name'):
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
