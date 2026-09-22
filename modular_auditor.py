# Smart Inventory Auditor
# Initialize inventory to zero
inventory = 0
# Variable for number of failed/rejected entries
failed_entries = 0

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

        # If inventory exceeds 500, an alert will be printed
        # The while loop will break
        if inventory > 500:
            print("Alert: Total inventory exceeded 500!")
            break
            
        else:
            print("Inventory updated")
            # Print current inventory total
            print("Inventory total:", inventory)

# After the while loop breaks, Total Units Processed and Number of Failed/Rejected Entries are printed
print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)