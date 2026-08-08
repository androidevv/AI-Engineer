invoice_no = input("Invoice No: ")
customer = input("Customer: ")
amount = float(input("Amount: "))

tax = amount * 0.18
total = amount + tax

print("\n--- Invoice ---")
print(f"Invoice No : {invoice_no}")
print(f"Customer   : {customer}")
print(f"Amount     : {amount:.2f}")
print(f"Tax        : {tax:.2f}")
print(f"Total      : {total:.2f}")