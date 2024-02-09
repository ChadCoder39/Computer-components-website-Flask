from flask import render_template, session, redirect, url_for, jsonify
from utils.json_group import cartDataByProdIds
from main import app

@app.route("/order_cart")
def order_cart():
    return render_template(
        "order_cart.html", 
        title="PCraft - Order Cart", 
        content=cartDataByProdIds(list(map(int, session.get('cart', []))))
    )

@app.route("/add_to_cart/<product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return jsonify(cart)


@app.route("/increase_quantity/<product_id>", methods=["POST"])
def increase_good_quantity(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return jsonify(cart)


@app.route("/decrease_quantity/<product_id>", methods=["POST"])
def decrease_good_quantity(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.pop(cart.index(product_id))
    session['cart'] = cart
    return jsonify(cart)


@app.route("/remove_from_cart/<product_id>", methods=["POST"])
def remove_good_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        del cart[product_id]
    session['cart'] = cart
    return jsonify(cart)


@app.route("/cart", methods=["GET"])
def cart():
    cart = cartDataByProdIds(list(map(int, session.get('cart', []))))
    return jsonify(cart)