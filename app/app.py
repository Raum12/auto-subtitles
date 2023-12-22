from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from subtitler import generate_translated_subs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/read-form', methods=['POST'])
def read_form():
   data = request.form
   
   return data["video_url"]

if __name__ == "__main__":
    app.run(debug=True)