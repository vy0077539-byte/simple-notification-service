from flask import Flask, request
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

BUCKET = os.environ.get("UPLOAD_BUCKET", "project-file-upload-bucket-vikas")
REGION = "eu-north-1"

s3 = boto3.client("s3", region_name=REGION)

@app.route("/", methods=["GET"])
def index():
    return '''
    <h2>Upload File to S3</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    '''

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    filename = secure_filename(file.filename)
    s3.upload_fileobj(file, BUCKET, filename)

    return "File uploaded successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
