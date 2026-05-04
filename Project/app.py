# Function to print final bill
def cli_cal(customer_name, items, subtotal, discount, tax, final_total, payment_method):

    print("\n============= Welcome to the CLI Billing System =============")
    print("Customer Name:", customer_name)
    print("Payment Method:", payment_method)
    print("-------------------------------------------------------------")

    # Loop to print each item
    for item in items:
        print("Product:", item["name"])
        print("Price:", item["price"])
        print("Quantity:", item["quantity"])
        print("Total:", item["total"])
        print("-------------------------------------------------------------")

    print("Total Items:", len(items))
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Total:", final_total)
    print("=============================================================")
    print("Thank you for shopping with us!")


# Taking customer name
customer_name = input("Enter customer name: ")

items = []          # list to store all products
subtotal = 0        # total before discount

# Loop to add multiple items
while True:
    product_name = input("\nEnter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Validation check
    if price <= 0 or quantity <= 0:
        print("Invalid price or quantity. Please try again.")
        continue

    # Calculate total of one item
    item_total = price * quantity

    # Store item in dictionary
    item = {
        "name": product_name,
        "price": price,
        "quantity": quantity,
        "total": item_total
    }

    # Add item to list
    items.append(item)

    # Update subtotal
    subtotal = subtotal + item_total

    # Ask user to continue or stop
    choice = input("Do you want to add more items? (yes/no): ")

    if choice.lower() != "yes":
        break


# Option to remove last item
remove_choice = input("\nDo you want to remove last item? (yes/no): ")

if remove_choice.lower() == "yes" and len(items) > 0:
    removed_item = items.pop()
    subtotal = subtotal - removed_item["total"]
    print("Removed item:", removed_item["name"])


# Apply discount
if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0


# Calculate tax and final total
amount_after_discount = subtotal - discount

#tax 5% of amount after discount
tax = amount_after_discount * 0.05


final_total = amount_after_discount + tax


# Payment method
payment_method = input("Enter payment method (cash/card): ")


# Final function call
cli_cal(customer_name, items, subtotal, discount, tax, final_total, payment_method)