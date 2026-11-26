# Grade 9 POS Ordering System
# Developer A - Product Menu and Ordering

products = {
    1: {"name": "Burger", "price": 50},
    2: {"name": "Fries", "price": 40},
    3: {"name": "Pizza", "price": 100},
    4: {"name": "Soft Drink", "price": 25},
    5: {"name": "Sandwich", "price": 60}
}

# Stores customer orders
orders = []


def display_menu():
    print("\n===== PRODUCT MENU =====")
    for number, product in products.items():
        print(f"{number}. {product['name']} - ₱{product['price']:.2f}")


def place_order():
    while True:
        display_menu()
        print("0. Finish Order")

        try:
            choice = int(input("\nSelect product number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if choice not in products:
            print("Invalid product selection.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        product = products[choice]
        subtotal = product["price"] * quantity

        orders.append({
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "subtotal": subtotal
        })

        print(f"{product['name']} added successfully!")
        print(f"Subtotal: ₱{subtotal:.2f}")

    print("\nOrder completed!")


# Run program
place_order()

print("\n===== ORDER SUMMARY =====")
for item in orders:
    print(f"{item['name']} x {item['quantity']} = ₱{item['subtotal']:.2f}")

total_amount = sum(item["subtotal"] for item in orders)
print(f"Total Amount: ₱{total_amount:.2f}")