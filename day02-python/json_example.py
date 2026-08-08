import json

customer = {
    "id": 1001,
     "name": "ABC Transport",
     "city": "Faisalabad",
     "balance": 150000
}

json_data = json.dumps(customer, indent=4)
print(json_data)