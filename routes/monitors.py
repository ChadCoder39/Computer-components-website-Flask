from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/monitors")
def monitors():
    return render_template(
        "monitors.html", 
        title="PCraft - Monitors",
        content=readJson('monitors.json')
    )