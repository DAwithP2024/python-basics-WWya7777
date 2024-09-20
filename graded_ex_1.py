
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def main():
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    cart = []
    while True:
        display_categories()
        choice = input("Select a category by number: ")
        if choice.isdigit() and int(choice) in range(1, len(products) + 1):
            choice = int(choice)
            category = list(products.keys())[choice - 1]
            products_list = products[category]
            while True:
                display_products(products_list)
                option = input("Choose an option (1-4): ")
                if option == '1':
                    product_choice = input("Select a product to buy by number: ")
                    if product_choice.isdigit() and int(product_choice) in range(1, len(products_list) + 1):
                        product_choice = int(product_choice)
                        quantity = int(input("Enter quantity: "))
                        add_to_cart(cart, products_list[product_choice - 1], quantity)
                elif option == '2':
                    sort_order = input("Sort by price: ascending (1) or descending (2): ")
                    sorted_products = display_sorted_products(products_list, sort_order)
                    display_products(sorted_products)
                elif option == '3':
                    break
                elif option == '4':
                    if cart:
                        display_cart(cart)
                        total_cost = sum(item['price'] * item['quantity'] for item in cart)
                        address = input("Enter delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return
        else:
            print("Invalid choice. Please try again.")

def display_categories():
    print("Categories:")
    for i, category in enumerate(products, start=1):
        print(f"{i}. {category}")

def display_products(products_list):
    for i, product in enumerate(products_list, start=1):
        print(f"{i}. {product[0]} - ${product[1]}")

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == '2'))

def add_to_cart(cart, product, quantity):
    cart.append({"name": product[0], "price": product[1], "quantity": quantity})

def display_cart(cart):
    print("Cart contents:")
    for item in cart:
        print(f"{item['name']} - ${item['price']} x {item['quantity']}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Items purchased:")
    for item in cart:
        print(f"{item['name']} - ${item['price']} x {item['quantity']}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

# 启动程序
main()