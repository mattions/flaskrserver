from flask import Flask, render_template, url_for
import subprocess
import uuid
import os
app = Flask(__name__)

if not os.path.exists("static/plots"):
    os.mkdir("static/plots")

@app.route("/rscript")
def rscript():
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
