from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/motherboards")
def motherboards():
    return render_template(
        "motherboards.html", 
        title="PCraft - Motherboards", 
        content=readJson('motherboards.json')
    )