from flask import render_template, session, redirect, url_for
from main import app

@app.route("/order_cart")
def order_cart():
    return render_template(
        "order_cart.html", 
        title="PCraft - Order Cart", 
        content="Order Cart Content"
    )

@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('cart'))


@app.route("/cart", methods =["GET"])
def cart():
    cart = session.get('cart', [])
    return render_template(
        "cart.html", 
        title="PCraft - Shopping Cart", 
        content="Shopping Cart Content", 
        cart=cart
    )