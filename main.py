# import json and os modules
import json
import os

# import Inventory, PhysicalProduct, DigitalProduct, CanBeShipped and Supplier classes
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from supplier import Supplier

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

                supplier_details = details["supplier"]

                supplier = Supplier(
                    supplier_id=supplier_details["supplier_id"],
                    name=supplier_details["name"],
                    contact_email=supplier_details["contact_email"]
                )

                product_type = details["type"]

                # If product type is physical product, a Physical Product object is created.
                if product_type == "physical":
                    product = PhysicalProduct(product_id, details["name"], float(details["price"]), int(details["stock"]), float(details["weight"]), supplier)

                # If product type is digital product, a Digital Product object is created.
                elif product_type == "digital":
                    product = DigitalProduct(product_id, details["name"], float(details["price"]), int(details["stock"]), float(details["download_size"]), supplier)

                # If product type is neither physical nor digital, invalid product type message is printed and the product is skipped.
                else:
                    print(f"Invalid product type for product ID {product_id}.")
                    continue

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
    if inventory.find_product(product_id) is not None:
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

    # User inputs for supplier
    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Email: ").strip()

    # Create a Supplier object
    supplier = Supplier(supplier_id, supplier_name, supplier_email)

    # User input for product type
    print("\nSelect Product Type:", 
          "\n1. Physical Product", 
          "\n2. Digital Product")
    
    product_type = input("Enter choice (1 or 2): ").strip()

    # If product type is physical product, prompt user for weight input.
    if product_type == "1":
        try:
            weight = float(input("Weight (kg): "))

            # If weight input is negative, error message is printed.
            if weight < 0:
                print("\nWeight cannot be negative.")
                return

        # If weight input is invalid, error message is printed.
        except ValueError:
            print("\nInvalid weight.")
            return

        # A Physical Product object is created.
        product = PhysicalProduct(product_id, product_name, price, stock, weight, supplier)

    # If product type is digital product, prompt user for download size input.
    elif product_type == "2":
        try:
            download_size = float(input("Download Size (MB): "))

            # If download size input is negative, error message is printed.
            if download_size < 0:
                print("\nDownload size cannot be negative.")
                return

        # If download size input is invalid, error message is printed.
        except ValueError:
            print("\nInvalid download size.")
            return

        # A Digital Product object is created.
        product = DigitalProduct(product_id, product_name, price, stock, download_size, supplier)

    # If product type input is invalid, error message is printed.
    else:
        print("\nInvalid product type.")
        return

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

    product = inventory.find_product(product_id)

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

    product = inventory.find_product(product_id)

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

def remove_product(inventory):
    """
    Function for removing product from inventory
    """

    print("\nRemove Product")

    # User input for product id to remove
    product_id = input("Enter Product ID to remove: ").strip()
    inventory.remove_product(product_id)

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

            supplier = product.get_supplier()

            saved_inventory[product_id]["supplier"] = {"supplier_id": supplier.get_supplier_id(), "name": supplier.get_supplier_name(), "contact_email": supplier.get_contact_email()}

            # If product is physical, the product type and weight are stored in the dictionary.
            if isinstance(product, PhysicalProduct):
                saved_inventory[product_id]["type"] = "physical"
                saved_inventory[product_id]["weight"] = product.get_weight()

            # If product is digital, the product type and download size are stored in the dictionary.
            elif isinstance(product, DigitalProduct):
                saved_inventory[product_id]["type"] = "digital"
                saved_inventory[product_id]["download_size"] = product.get_download_size()

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
    print("5. Remove Product")
    print("6. Save Inventory")
    print("7. Exit")
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

        # If option 5 is chosen, call remove_product(inventory) function
        elif menu_option == "5":
            remove_product(inventory)

        # If option 6 is chosen, call save_inventory(inventory) function
        elif menu_option == "6":
            save_inventory(inventory)

        # If option 7 is chosen, call save_inventory(inventory) function to save inventory and break from while loop exit the program
        elif menu_option == "7":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        # If menu option input is not any of the options 1-6, print error message and ask user to re-enter
        else:
            print("\nInvalid option. Please re-eneter options 1-7")

if __name__ == "__main__":
    main()