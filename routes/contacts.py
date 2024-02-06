from main import app
from flask import render_template


@app.route("/contacts")
def contacts():
    return render_template(
        "contacts.html", 
        title="PCraft - Contacts", 
        content="Contact Information"
    )