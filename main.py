from flask import Flask, render_template
from utils.readJson import readJson


app = Flask(__name__)


@app.route("/startpage")
def start_page():
    return render_template("start_page.html", title="Start Page", content="Start Page Content")

@app.route("/loyaltyprogram")
def loyalty_program():
    return render_template("loyalty_program.html", title="Loyalty Program", content="Loyalty Program Content")

@app.route("/order_cart")
def order_cart():
    return render_template("order_cart.html", title="Order Cart", content="Order Cart Content")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Contacts", content="Contact Information")

@app.route("/video_cards")
def video_cards():
    return render_template("video_cards.html", title="Video Cards", content=readJson('videocards.json'))

@app.route("/processors")
def processors():
    return render_template("processors.html", title="Processors", content="Processors Content")

@app.route("/ram")
def ram():
    return render_template("ram.html", title="RAM", content="RAM Content")

@app.route("/discs")
def discs():
    return render_template("discs.html", title="Discs", content="Discs Content")

@app.route("/motherboards")
def motherboards():
    return render_template("motherboards.html", title="Motherboards", content="Motherboards Content")

@app.route("/power_unit")
def power_unit():
    return render_template("power_unit.html", title="Power Unit", content="Power Unit Content")

@app.route("/cooling")
def cooling():
    return render_template("cooling.html", title="Cooling", content="Cooling Content")

@app.route("/cases")
def frame():
    return render_template("cases.html", title="Cases", content="Cases Content")

@app.route("/monitors")
def monitor():
    return render_template("monitors.html", title="Monitors", content="Monitors Content")

@app.route("/accessories")
def accessories():
    return render_template("accessories.html", title="Accessories", content="Accessories Content")

@app.route("/keyboards")
def keyboard():
    return render_template("keyboards.html", title="Keyboards", content="Keyboards Content")

@app.route("/mouses")
def mouse():
    return render_template("mouses.html", title="Mouses", content="Mouses Content")

@app.route("/mousepad")
def rug():
    return render_template("mousepad.html", title="Rug", content="Rug Content")

@app.route("/headphones")
def headphones():
    return render_template("headphones.html", title="Headphones", content="Headphones Content")

if __name__ == "__main__":
    app.run(debug=True)