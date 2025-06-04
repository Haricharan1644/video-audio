import os
from flask import Flask, request, jsonify, send_file
from moviepy.editor import VideoFileClip

app = Flask(__name__)
UPLOAD_FOLDER = "/app/shared/temp_files"

@app.route('/convert', methods=['POST'])
def convert_video_to_audio():
    data = request.get_json()
    filename = data.get("filename")
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_filename = filename.rsplit(".", 1)[0] + ".mp3"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)

    print(f"Input path: {input_path}")
    if not os.path.exists(input_path):
        return jsonify({"error": f"Input file not found: {input_path}"}), 400

    try:
        clip = VideoFileClip(input_path)
        clip.audio.write_audiofile(output_path)
        return send_file(output_path, as_attachment=True, mimetype="audio/mpeg")
    except Exception as e:
        print(f"Conversion error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
