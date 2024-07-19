from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        response = make_response(redirect(url_for('autorizate')))
        response.delete_cookie('Name')
        response.delete_cookie('Email')
        return response
    if request.cookies.get('Name'):
        return render_template('index.html', **request.cookies)
    else:
        return redirect(url_for('autorizate'))


@app.route('/autorizate', methods=['GET', 'POST'])
def autorizate():
    if request.method == 'POST':
        response = make_response(redirect(url_for('index')))
        name = request.form.get('Name')
        email = request.form.get('Email')
        print(name, email)
        response.set_cookie('Name', name)
        response.set_cookie('Email', email)
        return response
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
