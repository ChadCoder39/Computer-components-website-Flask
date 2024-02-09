const SERVER_BASE = 'http://127.0.0.1:5000'


export const httpFetchCart = async() => {
    return await axios.get(`${SERVER_BASE}/cart`);
}

export const httpAddToCart = async(productId) => {
    return await axios.post(`${SERVER_BASE}/add_to_cart/${productId}`);
}

export const httpRemoveFromCart = async(productId) => {
    return await axios.post(`${SERVER_BASE}/remove_from_cart/${productId}`);
}