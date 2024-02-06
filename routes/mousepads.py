from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/mousepads")
def mousepads():
    return render_template(
        "mousepads.html", 
        title="PCraft - Mousepads",
        content=readJson('mousepads.json')
    )