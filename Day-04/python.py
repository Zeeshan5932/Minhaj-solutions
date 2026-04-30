# Taking basic account information
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

# Storing in dictionary
account = {
    "name": name,
    "balance": balance
}

# Account types (fixed)
account_types = ("Saving", "Current")

print("Available account types:", account_types)
acc_type = input("Choose account type: ")

# List to store transactions
transactions = []

# Ask operation
operation = input("Enter operation (deposit/withdraw): ")

if operation == "deposit":
    amount = float(input("Enter deposit amount: "))
    account["balance"] += amount
    transactions.append(amount)
    print("Amount deposited successfully")

elif operation == "withdraw":
    amount = float(input("Enter withdraw amount: "))
    
    if amount <= account["balance"]:
        account["balance"] -= amount
        transactions.append(amount)
        print("Amount withdrawn successfully")
    else:
        print("Insufficient Balance")

else:
    print("Invalid operation")

# Set for unique transactions
unique_transactions = set(transactions)

# Final output
print("\n--- Bank Summary ---")
print("Name:", account["name"])
print("Account Type:", acc_type)
print("Final Balance:", account["balance"])
print("All Transactions:", transactions)
print("Unique Transactions:", unique_transactions)