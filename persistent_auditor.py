# Smart Inventory Auditor

# File used to store inventory data
INVENTORY_FILE = "inventory.txt"

# List to store every valid transaction amount
transaction_list = []

# Initialize inventory to zero
inventory = 0
# Variable for number of failed/rejected entries
failed_entries = 0

# Variable for number of deliveries processed
deliveries_processed = 0

# Variable for delivery amount
delivery_amount = 0

# Assuming the delivery amount is $1 per stock unit
delivery_unit_price = 1

# get_valid_input() function
def get_valid_input():
    # User input for stock quantity
    stock_input = input("Enter quantity: (or type 'quit' to exit)")

    # Changes stock_input to lowercase
    if stock_input.lower() == 'quit':
        return "quit"
    
    # Rejects inputs which are not integers
    elif not stock_input.isdigit():
        return None
    
    # Reject negative numbers
    elif int(stock_input) < 0:
        return None

    # Returns valid stock input
    else:
        return int(stock_input)

# process_delivery(current_total, new_value) function
def process_delivery(current_total, new_value):
    new_total = current_total + new_value*delivery_unit_price
    return new_total

# calculate_tax(amount) function
def calculate_tax(amount):
    # 10% tax of the specific delivery
    tax = round(amount * 0.10, 2)
    return tax

# generate_report(total_units, deliveries_processed, failed_attempts) function
def generate_report(total_units, deliveries_processed, failed_attempts):
    print("Summary Report")
    print("----------------")
    print("Total Units Processed: ", total_units)
    print("Total Deliveries Processed: ", deliveries_processed)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

#load_inventory() function
def load_inventory():
    # Open inventory file in read mode to load the total inventory and saved transaction history
    # If inventory file does not exist, return 0 and start with an empty transaction list
    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.readlines()

            # Get the total inventory from line 1
            if len(lines) >= 1:
                inventory = int(lines[0].strip())
            else:
                inventory = 0

            transaction_list = []

            for line in lines[1:]:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(",", 2)

                if len(parts) == 3:
                    product_id = int(parts[0].strip())
                    product_name = parts[1].strip()
                    quantity = int(parts[2].strip())

                    transaction_list.append({"product_id": product_id, "product_name": product_name, "quantity": quantity})

            # Return inventory and transaction_list
            return inventory, transaction_list
        
    except FileNotFoundError:
        return 0, []

# save_inventory(inventory, transaction_list) function
def save_inventory(inventory, transaction_list):
    # Open inventory file in write mode
    with open(INVENTORY_FILE, "w") as file:
        # Write total inventory to inventory.txt
        file.write(str(inventory) + "\n")

        # Write transaction history to inventory.txt
        for transaction in transaction_list:
            file.write(
                str(transaction["product_id"]) + "," + transaction["product_name"] + "," + str(transaction["quantity"]) + "\n"
            )

# Call load_inventory() function
inventory, transaction_list = load_inventory()

# Update number of deliveries processed based on the length of transaction_list
deliveries_processed = len(transaction_list)

# Calculate previous delivery amount
for transaction in transaction_list:
    delivery_amount += (
        transaction["quantity"] * delivery_unit_price
    )

# Print previously saved transactions
print("Current Orders:")
print()

if len(transaction_list) == 0:
    print("No transactions has been saved yet.")

else:
    for transaction in transaction_list:
        print(
            str(transaction["product_id"]) + ", " + transaction["product_name"] + ", " + str(transaction["quantity"])
        )

print()

# While loop
while True:

    print()
    # Get user input for product name
    product_name = input("Enter Product Name: (or type 'quit' to exit)")

    # If user quits, inventory and transactions will be saved
    if product_name.lower() == "quit":
        save_inventory(inventory, transaction_list)
        print()
        print("Order successfully saved to inventory.txt")
        print("Quitting the program.")
        break

    # If product_name input is empty, then increment failed_entries and print error
    elif product_name.strip() == "":
        failed_entries += 1
        print("Error: Please enter the product name")
        continue

    # Call get_valid_input() function
    stock_input = get_valid_input()

    # If user enters 'quit', the valid transactions will be saved and the while loop will break
    if stock_input == "quit":
        # Call save_inventory(inventory, transaction_list) function
        save_inventory(inventory, transaction_list)
        print()
        print("Order successfully saved to inventory.txt")
        print("Quitting the program.")
        break

    elif stock_input is None:
        failed_entries += 1
        print("Error: Please enter a valid stock quantity or type 'quit' to exit.")
        continue

    else:

        # Generate Product ID
        if len(transaction_list) == 0:
            product_id = 1001
        
        else:
            product_id = (transaction_list[-1]["product_id"] + 1)

        # Update inventory
        inventory += int(stock_input)

        transaction = {
            "product_id": product_id,
            "product_name": product_name,
            "quantity": int(stock_input)
        }

        # Update valid transaction to list
        transaction_list.append(transaction)

        # Update total number of deliveries processed
        deliveries_processed += 1

        # Call process_delivery(current_total, new_value) function to calculate delivery amount
        delivery_amount = process_delivery(delivery_amount, int(stock_input))

        # Call calculate_tax(amount) function to calculate tax for the current delivery
        tax = calculate_tax(int(stock_input)*delivery_unit_price)

        # If inventory exceeds 500, an alert will be printed
        # Inventory will be saved and the while loop will break
        if inventory > 500:
            print("Alert: Total inventory exceeded 500!")
            save_inventory(inventory, transaction_list)
            break
            
        else:
            print()
            print("New Order Added")
            print(str(product_id) + ", " + product_name + ", " + str(stock_input))
            print()
            print("Order successfully saved to inventory.txt")
            print()
            print("Inventory updated")
            # Print current inventory total
            print("Inventory total:", inventory)
            # Print total delivery amount
            print("Total delivery amount: $", delivery_amount)
            # Print tax for the current delivery
            print("Tax for current delivery: $", tax)

# After the while loop breaks, call generate_report(total_units, deliveries_processed, failed_attempts) function to print summary report
generate_report(inventory, deliveries_processed, failed_entries)