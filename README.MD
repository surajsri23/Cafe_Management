# ☕ Café Management System

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

A simple web application built with **Flask** and **Tailwind CSS** to manage a café's online ordering system. Features include browsing the menu, adding items to a cart, proceeding to checkout, and placing orders.

---

## 🚀 Features

- **Menu Display**: Browse food and drink items with images sourced from Unsplash.
- **Cart Functionality**: Add items to a cart and view the total cost.
- **Checkout**: Select a table number, enter a customer name, and place an order.
- **Responsive Design**: Works on mobile, tablet, and desktop devices.
- **Printable Bill**: Generate and print a bill from the cart.

---

## 📁 Project Structure

```plaintext
cafe-management/
├── static/
│   ├── css/
│   │   └── styles.css        # Compiled Tailwind CSS
│   ├── js/
│   │   └── script.js         # Client-side JavaScript
│   ├── images/               # (Optional) Local images if used
│   └── favicon.ico           # Favicon for the site
├── templates/
│   └── index.html            # Main HTML template
├── input.css                 # Tailwind CSS input file
├── app.py                    # Flask backend
├── tailwind.config.js        # Tailwind configuration
├── package.json              # Node.js dependencies
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ✅ Prerequisites
- Python 3.8+: For running the Flask app.

- Node.js 16+: For compiling Tailwind CSS.

- Git (optional): For version control.


## ⚙️ Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/surajsri23/Cafe_Management.git
cd cafe-management
```
2. Install Python Dependencies
```bash
pip install -r requirements.txt
```
3. Install Node.js Dependencies
```bash
npm install
```
4. Compile Tailwind CSS
Run this in one terminal to watch for changes:
```bash
npx tailwindcss -i input.css -o static/css/styles.css --watch
```
5. Run the Flask Application
Run this in another terminal:
```bash
python app.py
```
6. Access the Application
Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```
## 💡 Usage
- **Browse Menu**: Scroll to the "Our Menu" section and view available items.
- **Add to Cart**: Click "Add to Cart" on any item to add it to your cart.
- **View Cart**: Scroll to the "Your Cart" section to see your items and total.
- **Checkout**: Click "Proceed to Checkout," select a table, enter your name, and submit the order.
- **Print Bill**: From the cart, click "Print Bill" to generate a printable receipt.

## 📌 License
-This project is licensed under the MIT License.
-You are free to use, modify, and distribute this software with proper attribution.

## 👨‍💻 Author
- Suraj Srivastav
- GitHub: @surajsri23
