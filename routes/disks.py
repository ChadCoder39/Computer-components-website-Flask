from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/disks")
def disks():
    return render_template(
        "disks.html", 
        title="PCraft - Disks", 
        content=readJson('disks.json')
    )