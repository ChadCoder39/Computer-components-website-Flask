from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/cooling")
def cooling():
    return render_template(
        "cooling.html", 
        title="PCraft - Cooling", 
        content=readJson('cooling.json')
    )