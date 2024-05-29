from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def set_path(file):
    print(file)
    return f'Путь до файла: "{escape(file)}"'


if __name__ == '__main__':
    app.run()
