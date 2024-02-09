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
            await httpAddToCart(e.target.getAttribute('data-product_id')).then(({data}) => {
                updateCartButton(data.length);
            });
        });
    });

    // fetch and parse data from order cart
    (async() => {
        await httpFetchCart()
            .then(({data}) => {
                const productsAmount = data.map(i => i.amount).reduce((acc, curr) => acc + curr, 0)
                updateCartButton(productsAmount);
            });
    })();
});


function updateCartButton(x) {
    const cartBtnText = document.querySelector('#cart-btn-text');
    cartBtnText.innerHTML = x;
} 