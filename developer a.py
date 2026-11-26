menu = {
    1: ("Burger", 50.00),
    2: ("Fries", 35.00),
    3: ("Soft Drinks", 25.00)
}

print("===== FOOD MENU =====")
for number, (name, price) in menu.items():
    print(f"{number}. {name} - ₱{price:.2f}")

order = []
total = 0.0

while True:
    try:
        choice = int(input("\nSelect product number: "))
        quantity = int(input("Enter quantity: "))

        if choice not in menu:
            print("Invalid product number.")
            continue
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue

        name, price = menu[choice]
        subtotal = price * quantity
        order.append((name, quantity, subtotal))
        total += subtotal

    except ValueError:
        print("Please enter numbers only.")
        continue

    if input("Add another product? (y/n): ").lower() != "y":
        break
        
print("\n===== RECEIPT =====")
for name, quantity, subtotal in order:
    print(f"{name} x{quantity} - ₱{subtotal:.2f}")
print(f"TOTAL: ₱{total:.2f}")
