person_1 = {
    "first_name": "Andi",
    "last_name": "Pratama",
    "age": 20,
    "city": "Bandung",
}
person_2 = {
    "first_name": "Sari",
    "last_name": "Wulandari",
    "age": 22,
    "city": "Surabaya",
}
person_3 = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 19,
    "city": "Medan",
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")