import json

# Sample data
data = [
    {"user": "Alice", "details": {"age": 30, "birthdate": "1994-01-01"}},
    {"user": "Bob", "details": {"age": 25, "birthdate": "1999-05-15"}}
]

data2 = []
user = input("what is your name")
date = input("What is the date?")
data.append({"user":user, "date": date})

# Save to JSON
with open("data.json", "w") as f:
    json.dump(data, f)

# Retrieve from JSON
with open("data.json", "r") as f:
    loaded_data = json.load(f)

# Access a specific date
birthdate = loaded_data[1]["details"]["birthdate"]
print(birthdate) 
print(date)
print(loaded_data) # print whole data object
for person in loaded_data:
    print(f"here is {person['user']}")