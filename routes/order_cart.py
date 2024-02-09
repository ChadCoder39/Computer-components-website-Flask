from flask import render_template, session, redirect, url_for, jsonify
from utils.json_group import cartDataByProdIds
from main import app

@app.route("/order_cart")
def order_cart():
    return render_template(
        "order_cart.html", 
        title="PCraft - Order Cart", 
        content="Order Cart Content"
    )

@app.route("/add_to_cart/<product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return jsonify(cart)


@app.route("/cart", methods=["GET"])
def cart():
    cart = cartDataByProdIds(list(map(int, session.get('cart', []))))
    return jsonify(cart)