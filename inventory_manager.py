# import json and os modules
import json
import os

# inventory.json file
INVENTORY_FILE = "inventory.json"

# load_inventory() function
def load_inventory():

    # If inventory.json file exists, print inventory.json file found
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            # Open inventory.json file in read mode
            with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")
            return inventory

        # If there are operating system errors, print unable to load inventory and start with an empty inventory
        except (json.JSONDecodeError, OSError):
            print("Unable to load inventory.")
            print("Starting with an empty inventory.")
            return {}

    # If inventory.json file does not exist, return with an empty dictionary in the inventory
    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return {}

# add_product(inventory) function
def add_product(inventory):
    print("\nAdd New Product")

    # User input for product id
    product_id = input("Product ID: ").strip()

    #If product id already exists
    if product_id in inventory:
        print("Product already exists.")
        return

    # User input for product name
    product_name = input("Product Name: ").strip()

    try:
        # User inputs for price and stock quantity
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        # If price or stock is negative, print error message
        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    # If price or stock value is invalid, print error message
    except ValueError:
        print("Invalid price or stock quantity.")
        return

    # Add product to inventory dictionary
    inventory[product_id] = {
        "name": product_name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully.")

# update_stock(inventory) function
def update_stock(inventory):
    print("\nUpdate Stock")

    # User input for product id of stock to update
    product_id = input("Enter Product ID: ").strip()

    # If product_id does not exist in inventory, print product not found
    if product_id not in inventory:
        print("Product not found.")
        return
    
    product = inventory[product_id]

    # Print details of product to be updated
    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    try:
        # User input for new stock quantity of product
        new_stock = int(input("New Stock Quantity: "))

        # If new stock input is negative, print error message
        if new_stock < 0:
            print("Stock quantity cannot be negative.")
            return

    # If new stock input is invalid, print error message
    except ValueError:
        print("Invalid stock quantity.")
        return

    # Update stock quantity of product in inventory dictionary
    product["stock"] = new_stock

    print("Stock updated successfully.")

# search_product(inventory) function
def search_product(inventory):
    print("\nSearch Product")

    # User input for product id to search
    product_id = input("Enter Product ID: ").strip()

    # If product id does not exist in inventory, print product not found
    if product_id not in inventory:
        print("Product not found.")
        return

    # If product id exists in inventory, print product details
    else:
        product = inventory[product_id]

        print("Product Found")
        print("-" * 48)
        print(f"ID: {product_id}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("-" * 48)

# display_all(inventory) function
def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)

    # If inventory is empty, print inventory is empty
    if not inventory:
        print("Inventory is empty.")
        return

    # If inventory is not empty, print details of all the products in inventory
    else:
        # For loop to print the details of all the products in the inventory
        for product_id, product in inventory.items():
            print(
                f"ID: {product_id} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("-" * 48)

# save_inventory(inventory) function
def save_inventory(inventory):
    print("\nSaving Inventory...")

    try:
        # Open inventory.json file in write mode and save inventory to inventory.json
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    # If there are operating system errors, print unable to save inventory
    except OSError:
        print("Unable to save inventory.")

# while loop for executing the program
while True:
    print ("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print ("=" * 40)

    print()
    print("---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------")
    print()

    menu_option = input("Enter option: ").strip()