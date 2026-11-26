def generate_receipt(orders):

    print("\n" + "=" * 50)
    print(" RECEIPT")
    print(" MINI STORE")
    print("=" * 50)

    print(f"{'Product':<15}{'Qty':<5}{'Price':<12}{'Subtotal':<10}")
    print("-" * 50)

    total_amount = 0

    # Display all ordered products
    for item in orders:

        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        subtotal = item["subtotal"]

        print(f"{name:<15}{quantity:<5}{price:<12.2f}{subtotal:<10.2f}")

        # Calculate total amount
        total_amount += subtotal

    print("-" * 50)

    # Display total
    print(f"TOTAL AMOUNT: PHP {total_amount:.2f}")

    print("=" * 50)
    print(" THANK YOU FOR YOUR ORDER!")
    print("=" * 50)

    return total_amount


# SAMPLE TESTING
if __name__ == "__main__":

    sample_orders = [
        {"name": "Burger", "price": 50, "quantity": 2, "subtotal": 100},
        {"name": "Fries", "price": 35, "quantity": 1, "subtotal": 35},
        {"name": "Soft Drink", "price": 25, "quantity": 2, "subtotal": 50}
    ]
