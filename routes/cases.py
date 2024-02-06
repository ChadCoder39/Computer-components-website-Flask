from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/cases")
def cases():
    return render_template(
        "cases.html", 
        title="PCraft - Cases", 
        content=readJson('cases.json')
    )