from flask import Flask, render_template, url_for
import subprocess
import os
app = Flask(__name__)

@app.route("/rscript")
def rscript():
    image_path = url_for('static', filename='yunotwork.jpg')
    image_filename = "my_plot2.png"
    static_image_path = os.path.join("static", image_filename)
    #R --vanilla "--args static/blah3.png" < figure.R
    subprocess.call(["Rscript", "figure.R", static_image_path])
    image_path2 = url_for("static", filename=image_filename)
    return render_template("rscript.html", image_path=image_path2)

if __name__ == "__main__":
    app.run(debug=True)
