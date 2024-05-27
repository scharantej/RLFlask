
# Main Python Code for Flask Shopping Cart Application

# Import necessary modules
from flask import Flask, render_template, redirect, url_for, request, session

# Define the application
app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'YourSecretKeyHere'

# Define the products
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.00},
    {'id': 2, 'name': 'Product 2', 'price': 15.00},
    {'id': 3, 'name': 'Product 3', 'price': 20.00}
]

# Define the shopping cart
cart = {}

# Route to display the list of products
@app.route('/products')
def products():
    return render_template('product_list.html', products=products)

# Route to handle the Add to Cart button
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = int(request.form.get('product_id'))
    quantity = int(request.form.get('quantity'))
    
    # Add the product to the cart
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity}
    
    return redirect(url_for('products'))

# Route to display the shopping cart
@app.route('/cart')
def cart():
    return render_template('cart.html', cart=cart)

# Route to handle the update quantity and remove item buttons
@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_id = int(request.form.get('product_id'))
    quantity = int(request.form.get('quantity'))
    
    # Update the quantity or remove the product from the cart
    if quantity == 0:
        del cart[product_id]
    else:
        cart[product_id]['quantity'] = quantity
    
    return redirect(url_for('cart'))

# Route to display the checkout form
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Route to handle the checkout form submission
@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    # Process the checkout form
    # ... (Handle payment processing, order placement, etc.)

    # Clear the shopping cart
    session.clear()
    
    return redirect(url_for('products'))

# Main driver function
if __name__ == '__main__':
    app.run(debug=True)
