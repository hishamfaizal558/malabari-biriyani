from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    biryani = ["1. Chicken", "2. Mutton", "3. Beef", "4. Fish", "5. Veg"]
    drinks = ["1. Coke", "2. Pepsi", "3. Fanta", "4. Sprite", "5. 7up"]
    return render_template('index.html', biryani=biryani, drinks=drinks)

@app.route('/order', methods=['POST'])
def order():
    bprice = {"1": 190, "2": 260, "3": 200, "4": 120, "5": 100}
    dprice = {"1": 50, "2": 50, "3": 50, "4": 50, "5": 50}

    choice = request.form['biryani']
    choiced = request.form['drink']
    quantity = int(request.form['quantity'])  # Get the quantity from the form

    order = int(choice)
    orderd = int(choiced)

    biryani = ["1. Chicken", "2. Mutton", "3. Beef", "4. Fish", "5. Veg"]
    drinks = ["1. Coke", "2. Pepsi", "3. Fanta", "4. Sprite", "5. 7up"]

    # Calculate total price based on quantity
    total = (bprice[choice] * quantity) + dprice[choiced]

    return render_template(
        'order.html',
        biryani=biryani[order-1],
        drink=drinks[orderd-1],
        bprice=bprice[choice],
        dprice=dprice[choiced],
        quantity=quantity,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True)