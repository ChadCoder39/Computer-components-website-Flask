from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/processors")
def processors():
    return render_template(
        "processors.html", 
        title="PCraft - Processors", 
        content=readJson('processors.json')
    )