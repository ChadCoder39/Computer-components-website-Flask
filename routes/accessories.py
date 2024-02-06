from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/accessories")
def accessories():
    return render_template(
        "accessories.html", 
        title="PCraft - Accessories", 
        content=readJson('accessories.json')
    )