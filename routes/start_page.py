from main import app
from flask import render_template

@app.route("/start_page")
def start_page():
    return render_template(
        "start_page.html", 
        title="PCraft", 
        content="Start Page Content"
    )