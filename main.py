from flask import Flask, flash, request, redirect, url_for, render_template  # type: ignore
from werkzeug.utils import secure_filename  # type: ignore
from photo_restorer import predict_image
import os

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 16 MB

@app.route("/")
def home():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        restored_img_url = predict_image(file_path)
        return render_template(
            "index.html",
            filename=filename,
            restored_img_url=restored_img_url
        )
    else:
        flash('File type not allowed')
        return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
