# import json and os modules
import json
import os

# import Product and Inventory
from product import Product
from inventory import Inventory

# inventory.json file
INVENTORY_FILE = "inventory.json"

def load_inventory():
    """
    Function for loading inventory
    """

    inventory = Inventory()

    # If inventory.json file exists, inventory.json file found message is printed.
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            # inventory.json file is opened in read mode.
            with open(INVENTORY_FILE, "r") as file:
                saved_inventory = json.load(file)

            # If the saved inventory data in json file is not a dictionary, invalid inventory data and starting with an empty inventory messages are printed and inventory is returned.
            if not isinstance(saved_inventory, dict):
                print("Invalid inventory data.")
                print("Starting with an empty inventory.")
                return inventory

            # For every product in saved inventory data, each saved dictionary is converted to a Product object.
            for product_id, details in saved_inventory.items():
                product = Product(product_id, details["name"], float(details["price"]), int(details["stock"]))

                inventory.add_product(product)

            print("Inventory loaded successfully.")
            return inventory

        # If there are operating system errors, unable to load inventory and starting with an empty inventory messages are printed.
        except (json.JSONDecodeError, OSError):
            print("Unable to load inventory.")
            print("Starting with an empty inventory.")
            return Inventory()

    # If inventory.json file does not exist, inventory.json not found and starting with an empty inventory messages are printed and inventory is returned.
    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return inventory

def add_product(inventory):
    """
    Function for adding product
    """

    print("\nAdd New Product")

    # User input for product id
    product_id = input("Product ID: ").strip()

    #If product id already exists, product already exists message is printed.
    if inventory.search_product(product_id) is not None:
        print("\nProduct already exists.")
        return

    # User input for product name
    product_name = input("Product Name: ").strip()

    # If product_name input is empty, error message is printed.
    if not product_name:
        print("\nProduct Name cannot be empty.")
        return

    try:
        # User inputs for price and stock quantity
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        # If price or stock is negative, error message is printed.
        if price < 0 or stock < 0:
            print("\nPrice and stock cannot be negative.")
            return

    # If price or stock value is invalid, error message is printed.
    except ValueError:
        print("\nInvalid price or stock quantity.")
        return

    # A Product object is created.
    product = Product(product_id, product_name, price, stock)

    # If Product is added to inventory successfully, product added successfully message is printed.
    if inventory.add_product(product):
        print("\nProduct added successfully.")
    
    else:
        print("\nProduct already exists in inventory.")

def update_stock(inventory):
    """
    Function for updating stock in inventory
    """

    print("\nUpdate Stock")

    # User input for product id of stock to update
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    # If product id does not exist in inventory, product not found message is printed.
    if product is None:
        print("\nProduct not found.")
        return

    # Print details of product to be updated
    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        # User input for new stock quantity of product
        new_stock = int(input("\nNew Stock Quantity: "))

        # If new stock input is negative, error message is printed.
        if new_stock < 0:
            print("\nStock quantity cannot be negative.")
            return

    # If new stock input is invalid, error message is printed.
    except ValueError:
        print("\nInvalid stock quantity.")
        return

    # Stock quantity of the product is updated.
    product.update_stock(new_stock)

    print("\nStock updated successfully.")

def search_product(inventory):
    """
    Function for searching product in inventory
    """
    
    print("\nSearch Product")

    # User input for product id to search
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    # If product id does not exist in inventory, product not found message is printed.
    if product is None:
        print("\nProduct not found.")
        return

    # If product id exists in inventory, product details are printed.
    else:
        print("\nProduct Found")
        print("-" * 48)
        product.display_product_info()
        print("-" * 48)

def display_all(inventory):
    """
    Function for displaying all products in the inventory
    """

    inventory.display_all()

def save_inventory(inventory):
    """
    Function for saving inventory
    """

    print("\nSaving Inventory...")

    try:
        saved_inventory = {}

        # Get the product id of every product in the inventory and store the product details of every product in the dictionary.
        for product in inventory.get_products():
            product_id = product.get_product_id()

            saved_inventory[product_id] = {"name": product.get_name(), "price": product.get_price(), "stock": product.get_stock()}

        # Open inventory.json file in write mode and save inventory to inventory.json
        with open(INVENTORY_FILE, "w") as file:
            json.dump(saved_inventory, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    # If there are operating system errors, unable to save inventory message is printed.
    except OSError:
        print("Unable to save inventory.")

def main():
    """
    Function for executing the main program
    """

    # Call load_inventory() function
    inventory = load_inventory()

    print ("\n", "=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print ("=" * 40)

    # Print menu options
    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------")

    # while loop for executing the program
    while True:
        # User input for menu option
        menu_option = input("\nEnter option: ").strip()

        # If option 1 is chosen, call display_all(inventory) function
        if menu_option == "1":
            display_all(inventory)

        # If option 2 is chosen, call add_product(inventory) function
        elif menu_option == "2":
            add_product(inventory)

        # If option 3 is chosen, call update_stock(inventory) function
        elif menu_option == "3":
            update_stock(inventory)

        # If option 4 is chosen, call search_product(inventory) function
        elif menu_option == "4":
            search_product(inventory)

        # If option 5 is chosen, call save_inventory(inventory) function
        elif menu_option == "5":
            save_inventory(inventory)

        # If option 6 is chosen, call save_inventory(inventory) function to save inventory and break from while loop exit the program
        elif menu_option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        # If menu option input is not any of the options 1-6, print error message and ask user to re-enter
        else:
            print("\nInvalid option. Please re-eneter options 1-6")

if __name__ == "__main__":
    main()