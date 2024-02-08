'use strict'

// wait until the doc content completes loading
document.addEventListener('DOMContentLoaded', () => {
    // get all products
    const items = document.querySelectorAll('#product');
    // applying event listeners
    items.forEach(node => {
        // apply event on 'add to cart' button
        const btn = node.querySelector('#add-to-cart');
        // add event listener if btn with id 'add-to-cart' exists
        btn && btn.addEventListener('click', (e) => {
            e.preventDefault();
            console.log(`TODO: Code to add product into cart, PID: ${e.target.getAttribute('data-product_id')}`);
        });
    });
});