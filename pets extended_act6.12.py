pets = [
    {"kind": "cat", "owner": "Arya", "name": "Mimi", "age": 2},
    {"kind": "dog", "owner": "Sunoo", "name": "Bobi", "age": 4},
    {"kind": "rabbit", "owner": "Kama", "name": "Putih", "age": 1},
]

for pet in pets:
    print(f"{pet['name']} is a {pet['kind']}, {pet['age']} years old.")
    print(f"Owner: {pet['owner']}\n")