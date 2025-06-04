
from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "/app/shared/temp_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return jsonify({"message": "File uploaded successfully", "filename": filename}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)
