from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/headphones")
def headphones():
    return render_template(
        "headphones.html", 
        title="PCraft - Headphones", 
        content=readJson('headphones.json')
    )