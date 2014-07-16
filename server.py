from flask import Flask, render_template, url_for
import subprocess
import uuid
import os
import time

app = Flask(__name__)

SECONDS_IN_A_DAY = 86400

if not os.path.exists("static/plots"):
    os.mkdir("static/plots")

def cleanup_old_plot(path):
    now = time.time()
    for _, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(path, filename)
            mtime_file = os.stat(file_path).st_mtime
            print mtime_file
            if now - mtime_file > SECONDS_IN_A_DAY :
                os.remove(file_path)
        

@app.route("/rscript")
def rscript():
    cleanup_old_plot("static/plots")
    meme_path = url_for('static', filename='displayalltherplots.jpg')
    image_filename = "{0}_{1}".format("rplot", uuid.uuid4().hex)
    image_path = os.path.join("plots", image_filename)
    static_image_path = os.path.join("static", image_path)
    #R --vanilla "--args static/blah3.png" < figure.R
    subprocess.call(["Rscript", "figure.R", static_image_path])
    rimage_path = url_for("static", filename=image_path)
    return render_template("rscript.html", rimage_path=rimage_path, meme_image=meme_path)

if __name__ == "__main__":
    app.run(debug=True)
