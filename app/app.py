from flask import Flask, after_this_request, render_template, request, send_from_directory
from subtitler import generate_translated_subs
import os

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
    
    file_path = "upload_folder/video.mp4"
   
    generate_translated_subs(video_url)
    file_handle = open(file_path, 'r')
    
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
            file_handle.close()
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
   
    # return send_file("video.mp4", as_attachment=True)
    return send_from_directory(app.config['UPLOAD_FOLDER'], "video.mp4", as_attachment=True)
    # return redirect(url_for('download_file', name="video.mp4"))

if __name__ == "__main__":
    app.run(debug=True)