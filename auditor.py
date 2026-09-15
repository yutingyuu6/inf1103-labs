# Smart Inventory Auditor
# Initialize inventory to zero
inventory = 0

# While loop
while True:
    # User input for stock quantity
    stock_input = input("Enter stock quantity: (or type 'quit' to exit)")

    # Changes stock_input to lowercase
    # If user enters 'quit', the while loop will break
    if stock_input.lower() == 'quit':
        print("Quitting the program.")
        break

    # Rejects inputs which are not integers
    elif not stock_input.isdigit():
        print("Error: Please enter a valid stock quantity or type'quit' to exit.")
        continue

    # Reject negative numbers
    elif int(stock_input) < 0:
        print("Error: Stock quantity cannot be negative.")
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