from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
from subtitler import generate_translated_subs

app = Flask(__name__)

UPLOAD_FOLDER = "upload_folder"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/read-form', methods=['POST'])
def read_form():
    data = request.form
    video_url = data["video_url"]
   
    generate_translated_subs(video_url)
   
    # return send_file("video.mp4", as_attachment=True)
    return send_from_directory(app.config['UPLOAD_FOLDER'], "video.mp4", as_attachment=True)
    # return redirect(url_for('download_file', name="video.mp4"))

if __name__ == "__main__":
    app.run(debug=True)