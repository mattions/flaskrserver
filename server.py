from flask import Flask, render_template, url_for
import subprocess
app = Flask(__name__)

@app.route("/rscript")
def rscript():
    image_path = url_for('static', filename='yunotwork.jpg')
    image_filename = "my_plot.png"
    #R CMD BATCH figure.R "static/blah2.png"
    subprocess.call(["R", "CMD", "BATCH", "figure.R", image_filename])
    image_path2 = url_for("static", filename=image_filename)
    return render_template("rscript.html", image_path=image_path2)

if __name__ == "__main__":
    app.run(debug=True)
