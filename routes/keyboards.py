from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/keyboards")
def keyboards():
    return render_template(
        "keyboards.html", 
        title="PCraft - Keyboards", 
        content=readJson('keyboards.json')
    )