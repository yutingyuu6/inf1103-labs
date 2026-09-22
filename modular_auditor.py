# Smart Inventory Auditor
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
    stock_input = input("Enter stock quantity: (or type 'quit' to exit)")

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

# While loop
while True:
    # Call get_valid_input() function
    stock_input = get_valid_input()

    # If user enters 'quit', the while loop will break
    if stock_input == "quit":
        print("Quitting the program.")
        break

    elif stock_input is None:
        failed_entries += 1
        print("Error: Please enter a valid stock quantity or type 'quit' to exit.")
        continue

    else:
        # Update inventory
        inventory += int(stock_input)

        # Update total deliveries processed
        deliveries_processed += 1

        # Call process_delivery(current_total, new_value) function to calculate delivery amount
        delivery_amount = process_delivery(delivery_amount, int(stock_input))

        # Call calculate_tax(amount) function to calculate tax for the current delivery
        tax = calculate_tax(int(stock_input)*delivery_unit_price)

        # If inventory exceeds 500, an alert will be printed
        # The while loop will break
        if inventory > 500:
            print("Alert: Total inventory exceeded 500!")
            break
            
        else:
            print("Inventory updated")
            # Print current inventory total
            print("Inventory total:", inventory)
            # Print total delivery amount
            print("Total delivery amount: $", delivery_amount)
            # Print tax for the current delivery
            print("Tax for current delivery: $", tax)

# After the while loop breaks, call generate_report(total_units, deliveries_processed, failed_attempts) function to print summary report
generate_report(inventory, deliveries_processed, failed_entries)