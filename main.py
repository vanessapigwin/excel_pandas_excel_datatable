from flask import Flask, render_template, flash, request, redirect
from model_processing import process_files

ALLLOWED_EXTENSIONS = {'xls', 'xlsx'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLLOWED_EXTENSIONS


# ========================= App routes ============================ #

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        # if no file is selected, browser submits empty filename
        if file1.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file1 and allowed_file(file1.filename):
            table_html = process_files(file1, file2, file3)
            return render_template('result.html', table_html=table_html)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)