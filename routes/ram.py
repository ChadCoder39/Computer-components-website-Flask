from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/ram")
def ram():
    return render_template(
        "ram.html", 
        title="PCraft - RAM", 
        content=readJson('ram.json')
    )