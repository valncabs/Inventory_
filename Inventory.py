# Inventory system:
# This program requests the name, price, and quantity of a product,
# validates the data, calculates the total cost, and displays the result.

# Request product name
name = input("Enter the product name: ")

# Validate price (float)
valid_price = False

while valid_price == False:
    try:
        price = float(input("Enter the product price: "))
        if price > 0:
            valid_price = True
        else:
            print("Error: Price must be greater than 0.")
    except ValueError:
        print("Error: Enter a valid numeric value for price.")

# Validate quantity (int)
valid_quantity = False

while valid_quantity == False:
    try:
        quantity = int(input("Enter the product quantity: "))
        if quantity > 0:
            valid_quantity = True
        else:
            print("Error: Quantity must be greater than 0.")
    except ValueError:
        print("Error: Enter a valid integer value for quantity.")

# Calculate total cost
total_cost = price * quantity

# Show results
print("\n--- Result ---")
print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}")

# Final comment:
# This program allows registering a product in an inventory by requesting user input,
# validating the data using control variables, calculating the total cost, 
# and displaying the result.