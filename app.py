import os
from flask import Flask, render_template, request, json
from werkzeug.utils import secure_filename
from ImageParser import ImageParser
from searchEngine.Searcher import Searcher
import os.path

UPLOAD_FOLDER = '/query'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

app = Flask(__name__, static_url_path = "/dataset", static_folder = "dataset")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    imp = ImageParser()
    file = request.files['file']
    file.save(secure_filename(file.filename))
    img = imp.readImage(file.filename)
    features = imp.parseImage(img)
    searcher = Searcher("dataset.csv")
    results = searcher.searchIMG(features)

    os.remove(file.filename)
    return json.dumps({'status':'OK','data': results})

if os.path.isfile("dataset.csv") == False:
    print('start run dataset in first time')
    imp = ImageParser()
    imp.parseDataset()

if __name__ == "__main__":
    app.run()
