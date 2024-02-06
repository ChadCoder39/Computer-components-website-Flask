from main import app
from flask import render_template
from utils.readJson import readJson

@app.route("/video_cards")
def video_cards():
    return render_template(
        "video_cards.html", 
        title="PCraft - Video Cards", 
        content=readJson('videocards.json')
    )