## Task: Design Shopping Cart Web App

### HTML Files
- **product_list.html**: List of products with Add to Cart button for each product.
- **cart.html**: Displays the items in the shopping cart, along with options to update quantities and remove items.
- **checkout.html**: Form for user to provide shipping information and complete the purchase.

### Routes
- **@app.route('/products')**: Displays the list of products (product_list.html).
- **@app.route('/add_to_cart', methods=['POST'])**: Handles the Add to Cart button click, updating the cart session.
- **@app.route('/cart')**: Displays the shopping cart (cart.html).
- **@app.route('/update_cart', methods=['POST'])**: Handles the update quantity and remove item buttons in the cart, modifying the cart session.
- **@app.route('/checkout')**: Displays the checkout form (checkout.html).
- **@app.route('/process_checkout', methods=['POST'])**: Handles the checkout form submission and processes the purchase.