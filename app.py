from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu = {
    "Food": [
        {"name": "Classic Burger", "price": 5.99, "image": "https://images.unsplash.com/photo-1565299624946-baccd3051811"},
        {"name": "Margherita Pizza", "price": 8.99, "image": "https://images.unsplash.com/photo-1550547660-d9450f859349"},
        {"name": "Crispy Fries", "price": 2.99, "image": "https://images.unsplash.com/photo-1593560708920-61dd98c60f23"}
    ],
    "Drinks": [
        {"name": "Cappuccino", "price": 1.99, "image": "https://images.unsplash.com/photo-1512568400610-62da28bc8a57"},
        {"name": "Chilled Cola", "price": 1.49, "image": "https://images.unsplash.com/photo-1572490364222-13f0f8c0a768"},
        {"name": "Masala Tea", "price": 1.79, "image": "https://images.unsplash.com/photo-1606163026168-08f9e5b0eabf"}
    ]
}

orders = []

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    order_data = request.json
    if order_data:  # Check if order_data is not empty
        orders.append(order_data)
        return jsonify({"message": "Order placed successfully!", "order": order_data})
    else:  # If order_data is empty, return an error message
        return jsonify({"message": "No order data provided!"}), 400

if __name__ == '__main__':
    app.run(debug=True)