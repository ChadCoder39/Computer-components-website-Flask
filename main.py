from flask import Flask, render_template, session, url_for, redirect
from utils.readJson import readJson

app = Flask(__name__)
app.secret_key = '11122'


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
    return render_template("processors.html", title="Processors", content=readJson('processors.json'))


@app.route("/ram")
def ram():
    return render_template("ram.html", title="RAM", content=readJson('ram.json'))


@app.route("/disks")
def discs():
    return render_template("discs.html", title="Discs", content=readJson('discs.json'))


@app.route("/motherboards")
def motherboards():
    return render_template("motherboards.html", title="Motherboards", content=readJson('motherboards.json'))


@app.route("/power_unit")
def power_unit():
    return render_template("power_unit.html", title="Power Unit", content=readJson('power_unit.json'))


@app.route("/cooling")
def cooling():
    return render_template("cooling.html", title="Cooling", content=readJson('cooling.json'))


@app.route("/cases")
def frame():
    return render_template("cases.html", title="Cases", content=readJson('cases.json'))


@app.route("/monitors")
def monitor():
    return render_template("monitors.html", title="Monitors", content=readJson('monitors.json'))


@app.route("/accessories")
def accessories():
    return render_template("accessories.html", title="Accessories", content=readJson('accessories.json'))


@app.route("/keyboards")
def keyboard():
    return render_template("keyboards.html", title="Keyboards", content=readJson('keyboards.json'))


@app.route("/mouses")
def mouse():
    return render_template("mouses.html", title="Mouses", content=readJson('mouses.json'))


@app.route("/mousepad")
def rug():
    return render_template("mousepad.html", title="Rug", content=readJson('mousepad.json'))


@app.route("/headphones")
def headphones():
    return render_template("headphones.html", title="Headphones", content=readJson('headphones.json'))


#Cart
@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('cart'))


@app.route("/cart")
def cart():
    cart = session.get('cart', [])
    return render_template("cart.html", title="Shopping Cart", content="Shopping Cart Content", cart=cart)


if __name__ == "__main__":
    app.run(debug=True)