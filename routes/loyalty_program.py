from flask import render_template
from main import app

@app.route("/loyalty_program")
def loyalty_program():
    return render_template(
        "loyalty_program.html", 
        title="PCraft - Loyalty Program", 
        content="Loyalty Program Content"
    )