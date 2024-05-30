from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = b'99f3f1b11f29c1ca79f9cda98c9e071539e5c33b61854916ea1fa64bdffc6cac'


@app.route('/')
def index():
    if 'username' in session:
        return f'Hello, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
