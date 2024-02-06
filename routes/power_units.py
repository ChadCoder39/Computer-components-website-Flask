from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/power_units")
def power_units():
    return render_template(
        "power_units.html", 
        title="PCraft - Power Units", 
        content=readJson('power_units.json')
    )