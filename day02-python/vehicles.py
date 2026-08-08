vehicles = [
    {"number": "BSA-696", "type": "Diesel"},
    {"number": "ABC-123", "type": "Petrol"},
    {"number": "KLM-456", "type": "Diesel"},
]

for vehicle in vehicles:
    print (
    f"Vehicle: {vehicle['number']} |"
    f"Fuel {vehicle['type']}"
)

