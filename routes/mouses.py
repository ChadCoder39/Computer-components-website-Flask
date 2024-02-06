from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/mouses")
def mouses():
    return render_template(
        "mouses.html", 
        title="PCraft - Mouses", 
        content=readJson('mouses.json')
    )