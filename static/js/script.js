let cart = [];
let total = 0;

function addToCart(itemName, price) {
    cart.push({ name: itemName, price: price });
    total += price;
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';
    cart.forEach(item => {
        const div = document.createElement('div');
        div.className = 'flex justify-between';
        div.innerHTML = `<span>${item.name}</span><span>Rs${item.price.toFixed(2)}</span>`;
        cartItems.appendChild(div);
    });
    cartTotal.textContent = `Rs${total.toFixed(2)}`;
}

function proceedToCheckout() {
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }
    window.location.href = '#checkout';
}

function printBill() {
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }
    const customerName = document.getElementById('customer-name').value; // Get customer name
    let billContent = `Café Delight Bill\n\nCustomer: ${customerName}\n\nItems:\n`;
    cart.forEach(item => {
        billContent += `${item.name} - Rs${item.price.toFixed(2)}\n`;
    });
    billContent += `\nTotal: Rs${total.toFixed(2)}\n\nSignature: Cafe delight pvt ltd`; // Add signature line
    const printWindow = window.open('', '', 'width=600,height=400');
    printWindow.document.write(`
        <div style="border: 2px solid #000; padding: 10px; position: relative;">
            <div style="position: absolute; top: 0; left: 0; right: 0; text-align: center; opacity: 0.1; font-size: 50px; color: #000;">
                Cafe delight
            </div>
            <pre>${billContent}</pre>
        </div>
    `);
    printWindow.document.close();
    printWindow.print();
}

document.getElementById('checkout-form').addEventListener('submit', function (e) {
    e.preventDefault();
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }

    const tableNumber = document.getElementById('table-number').value;
    const customerName = document.getElementById('customer-name').value;

    const order = {
        table: tableNumber,
        customer: customerName,
        items: cart,
        total: total,
        timestamp: new Date().toISOString()
    };

    fetch('/place_order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(order)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        printBill(); // Automatically print the bill after order is placed
        cart = [];
        total = 0;
        updateCart();
        document.getElementById('checkout-form').reset();
        window.location.href = '#home';
    })
    .catch(error => console.error('Error:', error));
});