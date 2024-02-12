import os
import json
from flask import render_template, session, redirect, url_for, jsonify, request
from utils.json_group import cartDataByProdIds
from main import app


ORDERS_FILE_PATH = 'orders.json'


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
    
    cart_data = []
    for i in cart:
        if (i != product_id):
            cart_data.append(i)
        
    session['cart'] = cart_data
    return jsonify(cart_data)


@app.route("/submit_order", methods=["POST"])
def submit_order():
    try:
        if request.content_type != 'application/json':
            return jsonify({'error': 'Request must be in JSON format'}), 415

        order_data = request.get_json()

        if not order_data:
            return jsonify({'error': 'Empty request body'}), 400

        if 'email' not in order_data or 'products' not in order_data:
            return jsonify({'error': 'Invalid data format'}), 400

        email = order_data['email']
        products = order_data['products']

        if os.path.exists(ORDERS_FILE_PATH):
            with open(ORDERS_FILE_PATH, 'r') as file:
                orders = json.load(file)
        else:
            orders = {}

        orders[email] = products

        with open(ORDERS_FILE_PATH, 'w') as file:
            json.dump(orders, file, indent=4)

        return jsonify({'message': 'Order submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route("/cart", methods=["GET"])
def cart():
    cart = cartDataByProdIds(list(map(int, session.get('cart', []))))
    return jsonify(cart)