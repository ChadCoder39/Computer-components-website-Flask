'use strict'
import { httpAddToCart, httpDecreaseAmountInCart, httpFetchCart, httpIncreaseAmountInCart, httpRemoveFromCart } from "./requests.js";


// wait until the doc content completes loading
document.addEventListener('DOMContentLoaded', () => {
    // fetch and parse data from order cart
    (async() => {
        await httpFetchCart().then(({data}) => {
            const productsAmount = data.map(i => i.amount).reduce((acc, curr) => acc + curr, 0)
            updateCartButton(productsAmount);
            parseProducts(data);
            console.log(data)
        });
    })();
});


// function to update cart button products amount value
function updateCartButton(x) {
    const cartBtnText = document.querySelector('#cart-btn-text');
    cartBtnText.innerHTML = x;
} 

// function to get data-product-id from event emitter
function getDataProductIdProperty(e) {
    return e.target.getAttribute('data-product_id');
}


// function to properly display products on page and apply event listeners
function parseProducts(productsInCart) {
    // get all products
    const items = document.querySelectorAll('#product');
    // applying event listeners
    items.forEach(node => {
        // apply event on 'add to cart' button
        const btn = node.querySelector('#add-to-cart');
        const pid = btn.getAttribute('data-product_id');
        let inCart = productsInCart.map(i => i.product_id).includes(Number(pid));
        // add event listener if btn with id 'add-to-cart' exists
        if (btn) {
            // arrow function to update btn text 
            const updateBtnText = (productIsInCart) => {
                const btnSpan = btn.querySelector('#add-to-cart-text');
                btnSpan.innerHTML = productIsInCart ? 'Remove from cart' : 'Add to cart';
            }
            updateBtnText(inCart);

            // event listener on 'add to cart / remove from cart'
            btn.addEventListener('click', async(e) => {
                e.preventDefault();
                if (inCart) {
                    await httpRemoveFromCart(pid).then(({data}) => {
                        inCart = false;
                        updateBtnText(false);
                        updateCartButton(data.length);
                    })
                } else {
                    await httpAddToCart(pid).then(({data}) => {
                        inCart = true;
                        updateBtnText(true);
                        updateCartButton(data.length);
                    });
                }
            });

            // apply more event listeners if the order_cart page was opened
            if (location.pathname === '/order_cart') {
                // remove from cart
                const btnsRemoveFromCart = document.querySelectorAll('#remove-product');
                btnsRemoveFromCart.forEach(removeBtn => {
                    removeBtn.addEventListener('click', async(e) => {
                        e.preventDefault();
                        await httpRemoveFromCart(getDataProductIdProperty(e)).then(({data}) => {
                            console.log(data)
                        });
                    });
                });
    
                // increase amount
                const btnsIncreaseCount = document.querySelectorAll('#increase-product-amount');
                btnsIncreaseCount.forEach(increaseBtn => {
                    increaseBtn.addEventListener('click', async(e) => {
                        e.preventDefault();
                        await httpIncreaseAmountInCart(getDataProductIdProperty(e)).then(({data}) => {
                            console.log(data);
                        });
                    })
                });
    
                // decrease amount
                const btnsDecreaseCount = document.querySelectorAll('#decrease-product-amount');
                btnsDecreaseCount.forEach(decreaseBtn => {
                    decreaseBtn.addEventListener('click', async(e) => {
                        e.preventDefault();
                        await httpDecreaseAmountInCart(getDataProductIdProperty(e)).then(({data}) => {
                            console.log(data);
                        });
                    })
                });
            }
        }
    });
}