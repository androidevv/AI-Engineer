fuel_bills = [
    {
        "vehicle": "BSA-696",
        "fuel": "diesel",
        "liters": 340,
        "rate": 384,
    },

    {
            "vehicle": "ABC-123",
            "fuel": "diesel",
            "liters": 380,
            "rate": 387,
    },

    {
                "vehicle": "FDS-18-9696",
                "fuel": "diesel",
                "liters": 120,
                "rate": 360,
    },
]

def calculate_amount(liters, rate):
    return liters * rate


for bill in fuel_bills:
    amount = calculate_amount (
        bill["liters"],
        bill["rate"]
    )

print (
    f"{bill['vehicle']} | "
    f"{bill['fuel']} | | "
    f"{bill['liters']} | "
    f"Amount: Rs. {amount:,.2f}"
)

