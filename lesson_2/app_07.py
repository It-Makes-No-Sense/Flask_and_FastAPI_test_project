from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'File {file_name} uploaded successfully'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
