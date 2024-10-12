import json

# Sample data
data = [
    {"user": "Alice", "details": {"age": 30, "birthdate": "1994-01-01"}},
    {"user": "Bob", "details": {"age": 25, "birthdate": "1999-05-15"}}
]

# Save to JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Retrieve from JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# Access a specific date
birthdate = loaded_data[1]["details"]["birthdate"]
print(birthdate) 