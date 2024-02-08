'use strict'
import { httpAddToCart, httpFetchCart } from "./requests.js";

// wait until the doc content completes loading
document.addEventListener('DOMContentLoaded', () => {
    const page = location.pathname;

    // get all products
    const items = document.querySelectorAll('#product');
    // applying event listeners
    items.forEach(node => {
        // apply event on 'add to cart' button
        const btn = node.querySelector('#add-to-cart');
        // add event listener if btn with id 'add-to-cart' exists
        btn && btn.addEventListener('click', async(e) => {
            e.preventDefault();
            await httpAddToCart(e.target.getAttribute('data-product_id'));
        });
    });

    // fetch and parse data from order cart
    if (page === '/order_cart') {
        (async() => {
            const data = await httpFetchCart();
            console.log('Cart data: ', data)
        })();
    }
});