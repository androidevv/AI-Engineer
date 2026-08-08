customer = {
    "id": 1001,
    "name": "ABC Transport",
    "city": "Faisalabad",
    "balance": 150000,
    "active": True
}

print(customer["name"])
print(customer["balance"])

def calcuate_tax(amount, rate):
    return amount * rate / 100

amount = 100000
tax = calcuate_tax(amount, 18)

print("Amount: ", amount)
print("Tax: ", tax)
print("Total: ", amount + tax)