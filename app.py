from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu = {
    "Food": [
        {"name": "Classic Burger", "price": 99.00, "image": "/static/images/classic_burger.jpg"},
        {"name": "Margherita Pizza", "price": 199.00, "image": "/static/images/Margherita_Pizza.jpg"},
        {"name": "Crispy Fries", "price": 69.00, "image": "/static/images/Crispy_Fries.jpg"}
    ],
    "Drinks": [
        {"name": "Cappuccino", "price": 99.00, "image": "/static/images/Cappuccino.jpg"},
        {"name": "Chilled Cola", "price": 50.00, "image": "/static/images/cola.jpg"},
        {"name": "Masala Tea", "price": 50.00, "image": "/static/images/tea.jpg"}
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
